# Cosmetics Inventory & Expiration Tracker

## Overview
The Cosmetics Inventory & Expiration Tracker is a backend application that allows users to manage their personal cosmetic products and automatically track product expiration based on category-specific lifespan rules.

Users can securely store products, record when items are opened, and view expiration status (Fresh, Expiring Soon, or Expired) to reduce waste and avoid using unsafe products.

## Problem
Many cosmetics users own significantly more products than they can realistically track. Most people rely on memory or manually checking packaging that may not even have a clear expiration after opening label to determine whether a product is still safe to use. This often leads to:
* Using expired products
* Wasted money from forgotten items
* Cluttered collections with no visibility into expiration timelines

Additionally, cosmetics products have different timelines once opened (e.g., mascara expires much faster than foundation and liquid/cream-based products expire faster than powder-based products), making manual tracking inconsistent and error-prone.

## Solution
This application provides:
* Secure user authentication
* Product inventory management (CRUD)
* Category-based expiration rules
* Automatic expiration status calculation
* Filtering by expiration state

The core logic calculates expiration dynamically using:
* Product category lifespan rules
* Opened date (preferred)
* Purchase date fallback (if unopened)

## Core Features (MVP)
* User registration & login
* Add, edit, delete cosmetic products
* Predefined expiration rules by product category
* Automatic expiration status calculation
* Filter inventory by status (Fresh / Expiring Soon/ Expired)

## Tech Stack (Planned)
* Backend: Python (FastAPI)
* Database: PostgreSQL
* Authentication: JWT or session-based auth
* Deployment: TBD (render / Fly.io / AWS)

## Design Goals
* Clean, maintainable API design
* Clear data modeling with relational structure
* Extensible expiration rule logic
* Production-style validation and error handling
* Well-documented endpoints

## Future Improvements
* Email notifications for expiring products
* Admin-configurable category rules
* Barcode lookup integration
* Analytics dahsboard (usage trends, product turnover)
* Frontend interface

## Why I Built This
This project demonstrates the design and implementation of a real-world backend system with:
* Authentication
* Relational database modeling
* Time-based business logic
* RESTful API design
* Practical product thinking

The goal is to build a clean, scalable backend service that mirrors the kind of internal tooling or consumer platform systems used in production environments.
