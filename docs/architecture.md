# QuantForge Toolkit Architecture

## Overview

QuantForge Toolkit follows a modular architecture.

Each calculator is independent and reusable.

Validation logic is centralized inside the `validation`
package.

Unit tests are isolated inside the `tests`
directory.

The project is designed to support future portfolio
analytics modules without changing the public API.
