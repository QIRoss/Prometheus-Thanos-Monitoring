# Prometheus Thanos Monitoring

Studies based in day 45-46 of 100 Days System Design for DevOps and Cloud Engineers.

https://deoshankar.medium.com/100-days-system-design-for-devops-and-cloud-engineers-18af7a80bc6f

Days 41–50: Reliability Engineering

Day 45–46: Implement advanced monitoring and alerting strategies using Prometheus and Thanos.

## When to Use Prometheus:

* Basic Infrastructure Monitoring: If you're monitoring a small-scale system (e.g., a single data center or application cluster), Prometheus on its own is a great solution for tracking performance metrics, querying data, and triggering alerts.

* Service-Level Monitoring: When monitoring web services, APIs, or containerized applications, Prometheus can be used to ensure service availability, performance, and reliability.

* Alerting: Prometheus is useful for setting up alerts based on real-time metrics and trends, such as CPU, memory, disk usage, network performance, etc.

## When to Use Thanos:

* Multi-Region/Multi-Cluster Monitoring: If you're running multiple Prometheus servers in different regions or clusters and want a single aggregated view of all your metrics, Thanos is ideal.

* Long-Term Storage: If your use case requires you to store metrics for months or years (beyond Prometheus' usual retention limits), Thanos can  store this data in a cost-effective external storage.

* High Availability and Redundancy: If you need a highly available monitoring system where metrics remain accessible even if some Prometheus instances go down, Thanos ensures resiliency and replication.

* Large-Scale Monitoring: For large infrastructures with many Prometheus instances, Thanos is perfect for scaling up and centralizing your monitoring solution.

## Author
This project was implemented by [Lucas de Queiroz dos Reis][2]. It is based on the Day 23–24: Automate multi-environment setups using Terraform and Ansible dynamic inventories from the [100 Days System Design for DevOps and Cloud Engineers][1].

[1]: https://deoshankar.medium.com/100-days-system-design-for-devops-and-cloud-engineers-18af7a80bc6f "Medium - Deo Shankar 100 Days"
[2]: https://www.linkedin.com/in/lucas-de-queiroz/ "LinkedIn - Lucas de Queiroz"