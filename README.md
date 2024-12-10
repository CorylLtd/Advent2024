# Advent of Code Solutions 2024

Solutions for the 2024 puzzles on https://adventofcode.com/

```mermaid
graph TD
  subgraph Internet
    Client1[Client Device 1] --> Router
    Client2[Client Device 2] --> Router
  end
  
  Router --> Firewall
  
  subgraph DMZ
    Firewall --> LoadBalancer[Load Balancer]
    LoadBalancer --> WebServer1[Web Server 1]
    LoadBalancer --> WebServer2[Web Server 2]
  end

  Firewall --> AppServer[Application Server]
  AppServer --> DB[Database Server]
```