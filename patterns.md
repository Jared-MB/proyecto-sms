# SOA Design Patterns Summary

This document provides a structured summary of Service-Oriented Architecture (SOA) design patterns, categorized by their architectural scope and purpose.

## 1. Foundational Inventory Patterns
These patterns define the scope and logical structure of the service inventory within an organization.

### Inventory Boundary Patterns
* [cite_start]**Enterprise Inventory**: Establishes an enterprise-wide service architecture as the basis for a single service inventory[cite: 261, 267]. [cite_start]It standardizes services across the organization to maximize interoperability and recomposition[cite: 262].
* [cite_start]**Domain Inventory**: Used when a single enterprise inventory is unmanageable[cite: 316]. [cite_start]Services are grouped into domain-specific inventories, each standardized and governed independently[cite: 318, 337].

### Inventory Structure Patterns
* [cite_start]**Service Normalization**: Focuses on aligning service boundaries to minimize functional overlap and avoid redundant logic[cite: 439, 449]. [cite_start]It requires modeling services collectively to ensure distinct functional contexts[cite: 459].
* [cite_start]**Logic Centralization**: Ensures that reusable logic is accessed only through official agnostic services[cite: 514]. [cite_start]It prevents the proliferation of redundant logic by forcing consumers to use the designated service for a specific function[cite: 539, 540].
* [cite_start]**Service Layers**: Structures the inventory into logical layers (e.g., Utility, Entity, Task) based on functional types to ensure consistent modeling and design[cite: 608, 646].

## 2. Inventory Standardization Patterns
These patterns aim to establish fundamental design standards to ensure consistency and interoperability.

* [cite_start]**Canonical Protocol**: Establishes a single communication technology (e.g., HTTP/SOAP) as the primary medium for service interaction[cite: 717]. [cite_start]It avoids the need for bridging and ensures technological compatibility[cite: 715, 732].
* [cite_start]**Canonical Schema**: Standardizes data models for common information sets across all service contracts within an inventory[cite: 744]. [cite_start]This reduces the need for data transformation and design complexity[cite: 743, 751].

## 3. Inventory Centralization Patterns
These patterns physically centralize specific architectural aspects to improve governance and management.

* [cite_start]**Process Centralization**: Centralizes business process logic in a dedicated orchestration platform (middleware)[cite: 867, 876]. [cite_start]This facilitates the maintenance and evolution of complex workflows[cite: 877].
* [cite_start]**Schema Centralization**: Positions schemas as physically separate parts of the service contract so they can be shared across multiple services[cite: 890, 899].
* [cite_start]**Policy Centralization**: Isolates global or domain-specific policies (e.g., security, QoS) so they can be applied to multiple services, reducing redundancy in contracts[cite: 913, 926].
* [cite_start]**Rules Centralization**: Separates business rules from service logic, managing them in a dedicated repository or rules engine for centralized access and governance[cite: 941, 952].

## 4. Inventory Implementation Patterns
These patterns address physical implementation issues, infrastructure, and redundancy.

* [cite_start]**Dual Protocols**: Allows an inventory to support a primary (standard) protocol and a secondary protocol for services that cannot conform to the standard immediately[cite: 974, 982].
* [cite_start]**Canonical Resources**: Standardizes infrastructure resources (databases, security frameworks) to avoid unnecessary disparity and reduce governance burden[cite: 1005, 1014].
* [cite_start]**State Repository**: Writes state data to a dedicated database temporarily, allowing services to remain stateless during inactivity and saving memory[cite: 1020, 1029].
* [cite_start]**Stateful Services**: Uses dedicated utility services to manage state data or context, relieving business services from state management duties[cite: 1040, 1046].
* [cite_start]**Service Grid**: Defers state data to a grid of system services that provide high scalability, memory replication, and fault tolerance[cite: 1056, 1068].
* [cite_start]**Inventory Endpoint**: Abstracts capabilities into an endpoint service that acts as an official gateway for external consumers, protecting internal inventory integrity[cite: 1086, 1091].
* [cite_start]**Cross-Domain Utility Layer**: Establishes a common layer of utility services shared across multiple domain inventories to avoid redundancy[cite: 1106, 1114].

## 5. Inventory Governance Patterns
Patterns designed to facilitate the control, maintenance, and evolution of the inventory.

* [cite_start]**Canonical Expression**: Applies standardized naming conventions to service contracts to ensure consistency and prevent misinterpretation[cite: 1131, 1140].
* [cite_start]**Metadata Centralization**: Uses a service registry to centrally publish service metadata, enabling formal registration and discovery processes[cite: 1150, 1158].
* [cite_start]**Canonical Versioning**: Standardizes versioning rules and how version information is expressed within contracts to maintain interoperability[cite: 1173, 1181].

## 6. Foundational Service Patterns (Service Definition)
These patterns guide the identification and definition of logical boundaries for individual services.

* [cite_start]**Functional Decomposition**: Decomposes a large business problem into smaller, related problems (concerns) to identify logic suitable for service encapsulation[cite: 1233, 1251].
* [cite_start]**Service Encapsulation**: Encapsulates solution logic within a service to position it as an enterprise resource[cite: 1288, 1310].
* [cite_start]**Agnostic Context**: Isolates multi-purpose logic into separate services with distinct agnostic contexts[cite: 1373, 1409].
* [cite_start]**Non-Agnostic Context**: Encapsulates single-purpose logic (specific to a single task) into services within the inventory[cite: 1466, 1486].
* [cite_start]**Agnostic Capability**: Partitions agnostic service logic into well-defined capabilities that address common concerns[cite: 1533, 1558].

## 7. Service Implementation Patterns
Patterns that affect the internal structure and physical implementation of a service.

* [cite_start]**Service Façade**: Inserts a component (façade) between the contract and core logic to abstract the implementation and accommodate changes without breaking the contract[cite: 1603, 1622].
* [cite_start]**Redundant Implementation**: Deploys reusable services via redundant implementations to eliminate single points of failure and ensure high availability[cite: 1738, 1756].
* [cite_start]**Service Data Replication**: Provides services with their own dedicated databases containing replicated data from a central source to increase autonomy[cite: 1806, 1823].
* [cite_start]**Partial State Deferral**: Temporarily defers a subset of state data to another location to reduce memory consumption while keeping the service stateful[cite: 1860, 1881].
* [cite_start]**Partial Validation**: Designing consumers to validate only the relevant subset of data in a message, ignoring the rest to improve performance[cite: 1907, 1915].
* [cite_start]**UI Mediator**: Uses an intermediary service or agent to manage UI interactions, ensuring consistent user feedback regardless of backend latency[cite: 1928, 1936].

## 8. Service Security Patterns
Patterns specifically designed to secure service interactions and resources.

* [cite_start]**Exception Shielding**: Sanitizes unsafe exception data (like stack traces) and replaces it with safe error messages before returning them to the consumer[cite: 1959, 1966].
* [cite_start]**Message Screening**: Equip services with routines to inspect incoming messages for malicious content (injection attacks) before processing[cite: 1989, 1999].
* [cite_start]**Trusted Subsystem**: The service uses its own credentials to access backend resources, preventing consumers from accessing resources directly[cite: 2032, 2039].
* [cite_start]**Service Perimeter Guard**: Establishes an intermediate service in the perimeter network (DMZ) as the secure point of contact for external consumers[cite: 2061, 2068].

## 9. Service Contract Design Patterns
Techniques for defining and structuring service technical interfaces.

* [cite_start]**Decoupled Contract**: Physically separates the service contract from its implementation logic to allow independent evolution[cite: 2087, 2096].
* [cite_start]**Contract Centralization**: Forces consumers to access service logic *only* via the published contract, preventing direct access to implementation resources[cite: 2110, 2116].
* [cite_start]**Contract Denormalization**: Introduces a measured degree of redundancy (e.g., varying granularity) in the contract to accommodate different consumer requirements[cite: 2129, 2136].
* [cite_start]**Concurrent Contracts**: Creates multiple contracts for a single service implementation, each tailored to a specific type of consumer[cite: 2147, 2154].
* [cite_start]**Validation Abstraction**: Moves granular validation logic out of the contract (to the underlying logic) to extend the contract's longevity and flexibility[cite: 2172, 2180].

## 10. Legacy Encapsulation Patterns
Patterns for integrating and wrapping legacy systems.

* [cite_start]**Legacy Wrapper**: Creates a standardized service wrapper around proprietary legacy APIs to abstract technical complexity[cite: 2204, 2217].
* [cite_start]**Multi-Channel Endpoint**: Centralizes transformation and workflow logic in a service to support multiple delivery channels (e.g., mobile, web) for legacy systems[cite: 2227, 2242].
* [cite_start]**File Gateway**: Introduces a gateway service to handle file-based data exchanges with legacy systems that cannot use direct service invocation[cite: 2253, 2270].