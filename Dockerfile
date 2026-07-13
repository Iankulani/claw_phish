# ============================================
# 🦀 CLAW-PHISH v5.0.0 - Dockerfile
# Multi-stage build with Alpine Linux
# ============================================

FROM python:3.11-alpine as builder

# Install build dependencies
RUN apk add --no-cache \
    gcc \
    musl-dev \
    libffi-dev \
    openssl-dev \
    cargo \
    make \
    git \
    python3-dev \
    py3-pip \
    && pip install --upgrade pip

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python packages
RUN pip install --no-cache-dir -r requirements.txt

# ============================================
# Final Stage
# ============================================
FROM python:3.11-alpine

# Install runtime dependencies
RUN apk add --no-cache \
    nmap \
    curl \
    netcat-openbsd \
    openssh-client \
    whois \
    bind-tools \
    iptables \
    tcpdump \
    traceroute \
    nikto \
    bash \
    sudo \
    shadow \
    docker-cli \
    && pip install --no-cache-dir --upgrade pip

# Create non-root user
RUN addgroup -g 1000 claw && \
    adduser -D -u 1000 -G claw claw && \
    echo "claw:claw" | chpasswd && \
    echo "claw ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

# Copy Python packages from builder
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Create application directories
RUN mkdir -p /app/.claw_phish /app/reports /app/temp && \
    chown -R claw:claw /app

# Copy application
COPY --chown=claw:claw claw_phish.py /app/
COPY --chown=claw:claw scripts/ /app/scripts/

WORKDIR /app

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PATH="/usr/local/bin:${PATH}"

# Expose ports
EXPOSE 5000 8080 8000-9000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import requests; requests.get('http://localhost:5000', timeout=5)" || exit 1

# Run as non-root user
USER claw

ENTRYPOINT ["python", "/app/claw_phish.py"]
CMD []