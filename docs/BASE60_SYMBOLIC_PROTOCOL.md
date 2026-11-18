# Base-12 / Base-60 Symbolic Protocol

This document specifies the fictional mathematical language layer requested for the project. It is a consistent encoding convention for worldbuilding, visualization and simulation—not a claim that number symbolism encodes hidden laws of nature.

## Coordinate layers

| Layer | Meaning | Canonical representation |
|---|---|---|
| Base-12 | Spatial structure, sectors, nested regions | integer coordinates and 12-sector indices |
| Base-60 | Time, orbital phase, synchronization | sexagesimal integer/fraction fields |
| Geometry | Relationships among entities | typed graph edges and geometric transforms |
| Frequency | Signal/transmission descriptors | carrier Hz, modulation, amplitude, phase radians |
| Prime numbers | Unique identifiers and derivation inputs | canonical integer IDs; cryptographic use delegated to standard libraries |
| Sacred numbers | Fictional authorization and dynastic classes | enumerated metadata, never cryptographic strength |

## Canonical message envelope

A message should have a version, sender ID, destination ID, sequence number, timestamp, spatial coordinate, signal descriptor, payload encoding and integrity field. Serialize canonical fields before hashing or signing. Define byte order, Unicode normalization, integer ranges, overflow behavior and unknown-field handling.

## Security boundary

Do not create a custom cipher from base-60 digits, prime patterns or sacred-number sequences. For real confidentiality and authenticity, use established authenticated encryption and a vetted key derivation function. The symbolic layer may format public metadata, but it must not replace cryptographic keys, nonces, authentication tags or protocol review.
