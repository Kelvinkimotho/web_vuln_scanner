import ssl
import socket

def check_ssl(target):
    """Check SSL certificate info for a given target."""
    try:
        hostname = target.split('/')[0]  # Extract domain
        context = ssl.create_default_context()
        
        with socket.create_connection((hostname, 443), timeout=3) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
        
        return {"SSL Valid": bool(cert)}
    except Exception as e:
        return {"error": f"SSL check failed: {str(e)}"}
