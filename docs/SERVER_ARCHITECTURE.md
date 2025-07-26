# Server Architecture Documentation

<!-- DOCUMENT_METADATA
Document Type: Technical Server Architecture Documentation
Project: Markit Backend Server Application
Framework: Node.js with Fastify and TypeScript
Architecture Pattern: Modular Monolith with Plugin System
Database: PostgreSQL with Prisma ORM
Purpose: Comprehensive guide to backend architecture, API design, and server implementation
Last Updated: 2024
-->

<!-- KEYWORDS: Server-Architecture, Node.js, Fastify, TypeScript, PostgreSQL, Prisma, API-Design, Backend-Development, Markit -->

## Table of Contents

1. [Overview](#overview) - Server application overview and core functionality
2. [Technology Stack](#technology-stack) - Complete backend technology stack and frameworks
3. [Project Structure](#project-structure) - Server codebase organization and file structure
4. [Architecture Patterns](#architecture-patterns) - Design patterns and architectural approaches
5. [Data Layer](#data-layer) - Database design and data access patterns
6. [Application Layer](#application-layer) - Business logic and service architecture
7. [API Layer](#api-layer) - REST API design and route organization
8. [Authentication & Authorization](#authentication--authorization) - Security and access control
9. [External Integrations](#external-integrations) - Third-party service integrations
10. [Error Handling](#error-handling) - Error management and exception handling
11. [Testing Strategy](#testing-strategy) - Testing frameworks and patterns
12. [Deployment & Environment](#deployment--environment) - Deployment configuration and environment setup
13. [Performance & Scalability](#performance--scalability) - Performance optimization and scaling strategies
14. [Security Considerations](#security-considerations) - Security measures and best practices
15. [Development Workflow](#development-workflow) - Development processes and tooling

---

## Overview

<!-- SECTION_START: Server Application Overview -->
**Context**: The Markit server is a comprehensive backend application that powers a marketing strategy generation platform, enabling users to create detailed marketing briefs and receive AI-generated marketing strategies.

**Technical Foundation**: Built as a Node.js-based backend application using the Fastify framework, the server implements a modular monolith architecture pattern that facilitates easy scaling and potential microservices transition while maintaining development simplicity.

**Business Purpose**: The server serves as the core engine for a marketing strategy platform that transforms user-provided business information into comprehensive, AI-generated marketing strategies through a structured workflow.

### Core Business Functionality

**Marketing Brief Management System**
- **Purpose**: Handles the complete marketing brief creation process through structured data collection
- **Implementation**: Multi-step form processing system collecting business information, marketing goals, target audience, and available resources
- **Data Flow**: Progressive form completion with validation, storage, and aggregation of brief components
- **Business Value**: Systematic capture of business context for accurate strategy generation

**AI-Powered Strategy Generation Engine**
- **Purpose**: Transforms marketing briefs into comprehensive marketing strategies using artificial intelligence
- **Implementation**: OpenAI GPT-4 integration with custom prompts and structured response parsing
- **Process**: Brief analysis, AI prompt construction, strategy generation, content structuring, and storage
- **Business Value**: Automated creation of professional marketing strategies from business inputs

**User Management and Authentication System**
- **Purpose**: Manages user accounts, authentication, and role-based access control
- **Implementation**: JWT-based authentication with three-tier role system (User, Expert, Admin)
- **Features**: User registration, email verification, password management, role-based permissions
- **Business Value**: Secure user management with differentiated access levels for different user types

**Document Management and Delivery System**
- **Purpose**: Generates and delivers marketing strategy documents to users
- **Implementation**: PDF generation from markdown content with email delivery capabilities
- **Features**: Strategy formatting, PDF conversion, email templates, delivery tracking
- **Business Value**: Professional document delivery enhancing user experience and strategy utility

**Expert Review and Editing Workflow**
- **Purpose**: Enables expert users to review, validate, and edit AI-generated strategies
- **Implementation**: Role-based access system with editing capabilities and approval workflows
- **Features**: Strategy review interface, content editing, approval tracking, version management
- **Business Value**: Quality assurance and human oversight for AI-generated content

### Key Technical Characteristics

**Type Safety and Validation**
- **Implementation**: Full TypeScript implementation with strict typing configuration
- **Validation**: Zod schema validation for all API inputs and outputs
- **Benefits**: Compile-time error prevention, runtime validation, improved developer experience
- **Impact**: Reduced runtime errors, better maintainability, enhanced code documentation

**API-First Design Approach**
- **Implementation**: OpenAPI/Swagger documentation with automatic schema generation
- **Standards**: RESTful API design with consistent response patterns
- **Documentation**: Interactive API documentation with request/response examples
- **Benefits**: Clear API contracts, easy integration, comprehensive documentation

**Database-Driven Architecture**
- **Implementation**: PostgreSQL database with Prisma ORM for type-safe operations
- **Features**: Automatic migration management, type generation, query optimization
- **Benefits**: Type safety at database level, easy schema evolution, optimized queries
- **Impact**: Reliable data persistence, simplified database operations, reduced SQL errors

**Plugin-Based Modular Architecture**
- **Implementation**: Fastify's plugin system for modular development and service organization
- **Structure**: Each business domain encapsulated as independent plugin with clear boundaries
- **Benefits**: Separation of concerns, easy testing, simplified maintenance, potential microservices extraction
- **Impact**: Improved code organization, better team collaboration, enhanced scalability

**Production-Ready Implementation**
- **Features**: Comprehensive error handling, structured logging, automated testing, performance monitoring
- **Standards**: Industry best practices for security, performance, and reliability
- **Monitoring**: Request logging, error tracking, performance metrics, health checks
- **Benefits**: Reliable production operation, easy debugging, proactive issue detection
<!-- SECTION_END: Server Application Overview -->

---

## Technology Stack

<!-- SECTION_START: Backend Technology Stack -->
**Overview**: The Markit server technology stack is built on modern Node.js ecosystem tools, prioritizing performance, type safety, and developer productivity while maintaining production-grade reliability.

### Core Runtime and Framework Technologies

**Node.js Runtime Environment**
- **Purpose**: JavaScript runtime providing the foundation for server-side execution
- **Version**: Latest LTS version for stability and long-term support
- **Benefits**: High-performance asynchronous I/O, extensive ecosystem, mature tooling
- **Use Case**: Server application runtime, package management, build processes

**Fastify 5.0.0 - High-Performance Web Framework**
- **Purpose**: Fast and low-overhead web framework for building APIs and web services
- **Key Features**: High performance, schema-based validation, plugin architecture, async/await support
- **Benefits**: 2x faster than Express, built-in JSON schema validation, excellent TypeScript support
- **Use Case**: API route handling, middleware management, request/response processing, plugin system

**TypeScript - Static Type System**
- **Purpose**: Superset of JavaScript providing static type checking and enhanced developer experience
- **Configuration**: Strict typing enabled with comprehensive type coverage
- **Benefits**: Compile-time error detection, better IDE support, self-documenting code, refactoring safety
- **Use Case**: Application development, type safety, code documentation, team collaboration

**TypeScript Compiler (tsc) - Build Tool**
- **Purpose**: Compiles TypeScript source code to JavaScript for production deployment
- **Configuration**: Optimized build settings with source maps and module resolution
- **Benefits**: Fast compilation, incremental builds, source map generation, module bundling
- **Use Case**: Development builds, production compilation, type checking, code transformation

### Database and Data Management Technologies

**PostgreSQL - Primary Database System**
- **Purpose**: Robust, ACID-compliant relational database for persistent data storage
- **Features**: Advanced SQL support, JSON operations, full-text search, performance optimization
- **Benefits**: Data integrity, complex queries, scalability, reliability, extensive feature set
- **Use Case**: User data storage, marketing brief persistence, strategy content management, relational data modeling

**Prisma 6.6.0 - Database ORM and Toolkit**
- **Purpose**: Modern database toolkit providing type-safe database access and schema management
- **Features**: Type generation, query building, migration management, database introspection
- **Benefits**: Type safety, developer productivity, automatic migrations, optimized queries
- **Use Case**: Database operations, schema evolution, type-safe queries, data modeling

**Prisma Migrate - Database Schema Management**
- **Purpose**: Database migration system for schema evolution and version control
- **Features**: Automatic migration generation, rollback support, environment management
- **Benefits**: Safe schema changes, version control, team collaboration, deployment automation
- **Use Case**: Schema updates, database versioning, production deployments, development setup

**Custom Prisma Client Generation**
- **Purpose**: Generated TypeScript client with custom output configuration
- **Configuration**: Output to `generated/prisma` for better organization
- **Benefits**: Type-safe database access, auto-completion, compile-time validation
- **Use Case**: Database queries, type inference, development efficiency

### Validation and API Documentation Technologies

**Zod 3.24.2 - Schema Validation Library**
- **Purpose**: TypeScript-first schema validation with type inference capabilities
- **Features**: Runtime validation, type inference, custom validators, error handling
- **Benefits**: Type safety, runtime validation, excellent TypeScript integration, clear error messages
- **Use Case**: API request validation, response validation, form data validation, configuration validation

**Fastify Swagger - API Documentation Generation**
- **Purpose**: Automatic OpenAPI documentation generation integrated with Fastify
- **Features**: Schema-based documentation, interactive UI, automatic generation
- **Benefits**: Always up-to-date documentation, interactive testing, developer experience
- **Use Case**: API documentation, testing interface, client generation, API contracts

**Swagger UI - Interactive API Documentation**
- **Purpose**: Web-based interface for exploring and testing API endpoints
- **Features**: Interactive testing, request/response examples, authentication support
- **Benefits**: Easy API exploration, testing capabilities, onboarding tool
- **Use Case**: API testing, documentation browser, developer onboarding, debugging

**fastify-type-provider-zod 4.0.2 - Type Integration**
- **Purpose**: Bridge between Zod schemas and Fastify's type system
- **Features**: Automatic type inference, schema integration, validation pipeline
- **Benefits**: Seamless integration, type safety, reduced boilerplate, consistent validation
- **Use Case**: API endpoint type generation, validation pipeline, type inference

### Authentication and Security Technologies

**@fastify/jwt 9.0.4 - JSON Web Token Implementation**
- **Purpose**: JWT authentication and token management for secure API access
- **Features**: Token generation, verification, expiration handling, algorithm support
- **Benefits**: Stateless authentication, secure token handling, industry standard implementation
- **Use Case**: User authentication, API security, session management, authorization

**bcrypt 5.1.1 - Password Hashing Library**
- **Purpose**: Secure password hashing using adaptive hashing algorithm
- **Features**: Salt generation, configurable rounds, secure comparison
- **Benefits**: Password security, protection against rainbow table attacks, adaptive difficulty
- **Use Case**: User password storage, authentication verification, security compliance

**@fastify/cors 11.0.0 - Cross-Origin Resource Sharing**
- **Purpose**: CORS middleware for controlling cross-origin requests
- **Features**: Origin validation, credential support, preflight handling
- **Benefits**: Security control, browser compatibility, flexible configuration
- **Use Case**: Frontend integration, API security, browser policy compliance

**@fastify/rate-limit 10.2.2 - Rate Limiting Middleware**
- **Purpose**: Request rate limiting for API protection and abuse prevention
- **Features**: Configurable limits, sliding window, distributed support
- **Benefits**: DDoS protection, abuse prevention, resource protection, fair usage
- **Use Case**: API protection, abuse prevention, performance protection, security

### External Service Integration Technologies

**@ai-sdk/openai 1.3.22 - OpenAI API Integration**
- **Purpose**: Official OpenAI SDK for AI-powered marketing strategy generation
- **Features**: GPT-4 integration, streaming support, error handling, type safety
- **Benefits**: Reliable AI integration, modern API design, excellent TypeScript support
- **Use Case**: Marketing strategy generation, AI content creation, prompt engineering, response processing

**Resend 4.1.2 - Email Service Provider**
- **Purpose**: Modern email API for transactional email delivery
- **Features**: Template support, delivery tracking, webhook integration, analytics
- **Benefits**: Reliable delivery, developer-friendly API, comprehensive tracking, modern design
- **Use Case**: User verification emails, strategy delivery, notifications, communication

**md-to-pdf 5.2.4 - PDF Generation Library**
- **Purpose**: Converts markdown content to PDF documents for strategy delivery
- **Features**: Markdown parsing, styling support, custom templates, high-quality output
- **Benefits**: Professional document generation, customizable styling, reliable conversion
- **Use Case**: Strategy document generation, PDF export, document delivery, content formatting

### Development and Testing Technologies

**Node.js Test Runner - Built-in Testing Framework**
- **Purpose**: Native Node.js testing framework for unit and integration tests
- **Features**: Async/await support, test isolation, parallel execution, built-in assertions
- **Benefits**: No external dependencies, fast execution, modern API, native integration
- **Use Case**: Unit testing, integration testing, test automation, continuous integration

**c8 Coverage Reporter - Code Coverage Analysis**
- **Purpose**: Provides comprehensive code coverage reporting for testing
- **Features**: V8 coverage integration, multiple output formats, threshold enforcement
- **Benefits**: Accurate coverage analysis, performance optimization, quality assurance
- **Use Case**: Test coverage analysis, quality metrics, CI/CD integration, development feedback

**Concurrently - Parallel Process Management**
- **Purpose**: Runs multiple development processes simultaneously
- **Features**: Process orchestration, output management, cross-platform support
- **Benefits**: Efficient development workflow, process coordination, simplified scripts
- **Use Case**: Development server, build watching, parallel compilation, workflow automation

**tsconfig-paths - Module Path Resolution**
- **Purpose**: Runtime module resolution for TypeScript path mapping
- **Features**: Path alias resolution, runtime support, configuration integration
- **Benefits**: Clean imports, better organization, simplified module management
- **Use Case**: Module resolution, import aliases, code organization, development experience
<!-- SECTION_END: Backend Technology Stack -->

---

## Project Structure

<!-- SECTION_START: Server Project Organization -->
**Overview**: The Markit server follows a modular monolith architecture with clear separation of concerns, domain-driven organization, and plugin-based structure for maintainability and scalability.

### Root Directory Structure

**Server Application Root:**
```
server/
├── src/                         # TypeScript source code
├── prisma/                      # Database schema and migrations
├── test/                        # Test files and test utilities
├── generated/                   # Auto-generated files (Prisma client)
├── dist/                        # Compiled JavaScript output
├── package.json                 # Project dependencies and scripts
└── tsconfig.json               # TypeScript configuration
```

### Source Code Organization (`src/`)

**Application Entry Point**
- **`app.ts`** - Main application entry point and Fastify server setup
  - **Purpose**: Initializes Fastify server, registers plugins, configures middleware
  - **Content**: Server configuration, plugin registration, startup logic
  - **Responsibilities**: Application bootstrap, environment setup, server lifecycle

**Configuration Management (`config/`)**
- **Purpose**: Centralized configuration for external services and application settings
- **Organization**: Service-specific configuration files with type-safe validation

**Configuration Files:**
- **`ai.ts`** - OpenAI model configuration and prompt templates
  - **Content**: GPT-4 model setup, prompt engineering, AI service configuration
  - **Purpose**: AI service integration, model selection, prompt management
  
- **`email.ts`** - Resend email service configuration and templates
  - **Content**: Email service setup, template definitions, delivery configuration
  - **Purpose**: Email service integration, template management, delivery settings
  
- **`env.ts`** - Environment variable validation using Zod schemas
  - **Content**: Environment schema definition, validation logic, type generation
  - **Purpose**: Type-safe environment configuration, runtime validation

**Application Constants (`constants/`)**
- **Purpose**: Application-wide constants, enumerations, and static values
- **Organization**: Grouped by functionality and usage domain

**Constants Files:**
- **`general.ts`** - HTTP status codes, API tags, and general application constants
  - **Content**: Status code definitions, API categorization, shared constants
  - **Purpose**: Consistent status codes, API organization, shared values

**Database Utilities (`db/`)**
- **Purpose**: Database-related utilities, seeding, and database-specific constants
- **Organization**: Database operations separate from business logic

**Database Files:**
- **`constants.ts`** - Database enumerations and default values
  - **Content**: Database enum definitions, default data values, constraint constants
  - **Purpose**: Database configuration, default data management, constraint definitions
  
- **`seed.ts`** - Database seeding script for development and testing
  - **Content**: Default data insertion, development setup, test data creation
  - **Purpose**: Development environment setup, test data management, initial data population

### Business Logic Modules (`modules/`)

**Modular Architecture**: Each business domain encapsulated as independent module with clear boundaries and responsibilities.

**Authentication Module (`auth/`)**
- **Purpose**: User authentication, authorization, and session management
- **Components**: User registration, login, email verification, password management
- **Structure**: Controller, service, validation, constants following standard module pattern

**Marketing Brief Modules (`brief/`)**
- **Purpose**: Marketing brief creation process through structured data collection
- **Organization**: Subdomain per brief step for clear separation of concerns

**Brief Submodules:**
- **`business-informations/`** - Company details and business setup information
- **`competitors/`** - Competitor analysis and competitive landscape data
- **`marketing-goals/`** - Marketing objectives and strategic goal definition
- **`marketing-resources/`** - Budget allocation and available marketing resources
- **`strategy-adjustments/`** - Success metrics and strategy adjustment preferences
- **`target-audiences/`** - Customer demographics and target market definition

**Default Data Modules (`default/`)**
- **Purpose**: Predefined data options for dropdowns, selections, and default values
- **Organization**: Category-based modules for different types of default data

**Default Data Categories:**
- **`channel/`** - Marketing channel options and definitions
- **`content/`** - Content type options and templates
- **`metric/`** - Success metric options and measurement types
- **`model/`** - Business model options and classifications
- **`objective/`** - Marketing objective templates and categories
- **`size/`** - Business size classifications and options
- **`tone/`** - Brand tone options and communication styles

**Strategy Management Module (`strategy/`)**
- **Purpose**: Marketing strategy generation, editing, and delivery
- **Organization**: Functional submodules for different strategy operations

**Strategy Submodules:**
- **`blocks/`** - Strategy content block management and structure
- **`download/`** - PDF generation and document download functionality
- **`send/`** - Email delivery and strategy distribution

### Infrastructure Components

**Fastify Plugins (`plugins/`)**
- **Purpose**: Reusable Fastify plugins for cross-cutting concerns
- **Organization**: Feature-specific plugins with clear responsibilities

**Plugin Files:**
- **`jwt.ts`** - JWT authentication plugin with token management
  - **Content**: JWT configuration, token validation, authentication middleware
  - **Purpose**: Authentication setup, token handling, security middleware
  
- **`prisma.ts`** - Prisma database plugin with connection management
  - **Content**: Database connection setup, client configuration, connection lifecycle
  - **Purpose**: Database integration, connection management, service decoration

**API Route Definitions (`routes/`)**
- **Purpose**: HTTP route definitions organized by business domain
- **Organization**: Domain-specific route registration with plugin pattern

**Route Modules:**
- **`auth/`** - Authentication and user management endpoints
- **`brief/`** - Marketing brief creation and management endpoints
- **`default/`** - Default data retrieval endpoints
- **`example/`** - Example and development endpoints
- **`strategy/`** - Strategy generation and management endpoints
- **`root.ts`** - Root-level routes and health check endpoints

**Utility Functions (`utils/`)**
- **Purpose**: Shared utility functions and helper methods
- **Organization**: Functionality-based organization with clear responsibilities

**Utility Files:**
- **`error-handler.ts`** - Global error handling and error response formatting
  - **Content**: Error processing, response formatting, logging integration
  - **Purpose**: Centralized error handling, consistent error responses
  
- **`general.ts`** - General-purpose utility functions and helpers
  - **Content**: Data transformation, validation helpers, common operations
  - **Purpose**: Shared functionality, data processing, common operations

### Database and Generated Files

**Database Schema (`prisma/`)**
- **`schema.prisma`** - Prisma schema definition with entity relationships
  - **Content**: Database model definitions, relationships, constraints
  - **Purpose**: Database structure, type generation, migration source
  
- **`migrations/`** - Database migration files and schema evolution history
  - **Content**: Migration scripts, schema changes, rollback information
  - **Purpose**: Schema versioning, deployment automation, database evolution

**Generated Files (`generated/`)**
- **Purpose**: Auto-generated TypeScript files from Prisma schema
- **Content**: Prisma client, type definitions, query builders
- **Management**: Automatically generated, not manually edited, version controlled

**Compiled Output (`dist/`)**
- **Purpose**: Compiled JavaScript output from TypeScript source
- **Content**: Transpiled JavaScript files, source maps, module outputs
- **Management**: Build artifacts, deployment target, not version controlled

### Module Structure Pattern

**Standard Module Organization**: Each business module follows consistent structure for predictability and maintainability:

```typescript
modules/[domain]/
├── index.ts              # Fastify plugin registration and module exports
├── controller.ts         # Request/response handling and HTTP logic
├── service.ts           # Business logic implementation and coordination
├── validation.ts        # Zod schema definitions for validation
└── constants.ts         # Module-specific constants and enumerations
```

**File Responsibilities:**
- **index.ts** - Plugin registration, dependency injection, route registration
- **controller.ts** - HTTP request handling, response formatting, input validation
- **service.ts** - Business logic, data processing, external service coordination
- **validation.ts** - Request/response validation schemas, type inference
- **constants.ts** - Module constants, enumerations, default values

**Benefits of Modular Structure:**
- **Clear Boundaries**: Each module has well-defined responsibilities and interfaces
- **Independent Development**: Modules can be developed and tested independently
- **Easy Maintenance**: Changes are localized to specific modules
- **Scalability**: Modules can be extracted to microservices if needed
- **Team Collaboration**: Clear ownership and responsibility boundaries
<!-- SECTION_END: Server Project Organization -->

---

## Architecture Patterns

### 1. Modular Monolith
The application follows a **modular monolith** pattern where each business domain is encapsulated in its own module with clear boundaries:

```typescript
// Module structure example
modules/
├── auth/
│   ├── index.ts          # Fastify plugin registration
│   ├── controller.ts     # Request/response handling
│   ├── service.ts        # Business logic
│   ├── validation.ts     # Zod schemas
│   └── constants.ts      # Module-specific constants
```

### 2. Plugin Architecture
Fastify's plugin system provides:
- **Encapsulation**: Each module is a self-contained plugin
- **Dependency Injection**: Services decorated on Fastify instance
- **Lifecycle Management**: Proper startup/shutdown hooks

```typescript
// Plugin registration pattern
const authPlugin: FastifyPluginAsync = async (fastify, opts) => {
  fastify.decorate("authService", new AuthService(fastify.prisma));
  fastify.decorate("authController", new AuthController(fastify.authService));
  
  // Route registration with schema validation
  fastify.post(authRoutes.signUp, authSchema.signUp, fastify.authController.signUp);
};
```

### 3. Layered Architecture
- **API Layer**: Route handlers, request/response transformation
- **Service Layer**: Business logic implementation
- **Data Layer**: Prisma ORM, database interactions
- **Validation Layer**: Zod schemas for type safety

### 4. Dependency Injection
Services are injected via Fastify's decorator pattern:

```typescript
declare module "fastify" {
  interface FastifyInstance {
    prisma: PrismaClient;
    authService: AuthService;
    briefService: BriefService;
  }
}
```

---

## Data Layer

### Database Design
The application uses **PostgreSQL** with **Prisma ORM** for type-safe database operations.

#### Core Entities

```prisma
model User {
  id                   Int                   @id @default(autoincrement())
  email                String                @unique
  fullName             String
  password             String
  verified             Boolean               @default(false)
  role                 Role                  @default(user)
  tier                 Tier                  @default(one)
  // Relationships to all user-generated content
  briefs               Brief[]
  businessInformations BusinessInformation[]
  // ... other relationships
}

model Brief {
  id                    Int                  @id @default(autoincrement())
  userId                Int
  // References to all brief components
  businessInformationId Int?                 @unique
  marketingGoalId       Int?                 @unique
  targetAudienceId      Int?                 @unique
  // ... other component references
  aiStrategy            AIStrategy?
}
```

#### Key Relationships
- **User**: Central entity with one-to-many relationships to all user content
- **Brief**: Aggregates all marketing brief components
- **AIStrategy**: Generated strategy with hierarchical block/section structure
- **Default Data**: Predefined options for dropdowns and selections

### Data Access Patterns

#### Service Layer Pattern
```typescript
export class BriefService {
  constructor(private db: PrismaClient) {}

  async create(userId: number, data: BriefCreateData) {
    return await this.db.brief.create({
      data: { userId, ...data },
      include: { user: true, aiStrategy: true }
    });
  }

  async getByUserId(userId: number) {
    return await this.db.brief.findMany({
      where: { userId },
      include: this.getFullBriefIncludes()
    });
  }
}
```

#### Transaction Management
Prisma handles transactions automatically, with explicit transaction support for complex operations:

```typescript
async updateStrategyWithBlocks(strategyId: number, blocks: BlockData[]) {
  return await this.db.$transaction(async (tx) => {
    await tx.aIStrategyBlock.deleteMany({ where: { strategyId } });
    return await tx.aIStrategyBlock.createMany({
      data: blocks.map(block => ({ strategyId, ...block }))
    });
  });
}
```

---

## Application Layer

### Service Architecture
Services encapsulate business logic and coordinate between data access and external services.

#### Core Services

```typescript
// Authentication Service
export class AuthService {
  async signUp(data: SignUpData) {
    const hashedPassword = await bcrypt.hash(data.password, 12);
    const user = await this.db.user.create({
      data: { ...data, password: hashedPassword }
    });
    await this.sendVerificationEmail(user);
    return user;
  }
}

// Strategy Service with AI Integration
export class StrategyService {
  async generateStrategy(briefId: number) {
    const brief = await this.getBriefWithAllComponents(briefId);
    const aiResponse = await generateText({
      model: openAIModel,
      prompt: this.buildStrategyPrompt(brief)
    });
    return await this.parseAndSaveStrategy(briefId, aiResponse);
  }
}
```

### Business Logic Patterns

#### Domain-Driven Design Elements
- **Aggregates**: Brief as an aggregate root with component entities
- **Value Objects**: Enums for status, roles, tiers
- **Domain Services**: Strategy generation, email notifications

#### Error Handling Strategy
```typescript
export class APIError extends Error {
  constructor(
    message: string,
    public error: string,
    public statusCode: number
  ) {
    super(message);
    Error.captureStackTrace(this, this.constructor);
  }
}

// Usage in services
if (!user.verified) {
  throw new APIError(
    "Email not verified",
    "Unauthorized",
    StatusCodes.Unauthorized
  );
}
```

---

## API Layer

### Route Organization
Routes are organized by domain and registered as Fastify plugins:

```typescript
// Domain-specific route registration
const briefRoutes: FastifyPluginAsync = async (fastify) => {
  fastify.register(businessInformationRoutes);
  fastify.register(marketingGoalsRoutes);
  fastify.register(targetAudienceRoutes);
  // ... other brief components
};
```

### Schema Validation
All endpoints use Zod schemas for request/response validation:

```typescript
export const authSchema = {
  signUp: {
    schema: {
      body: z.object({
        email: z.string().email(),
        fullName: z.string().min(2),
        password: z.string().min(8)
      }),
      response: {
        201: z.object({
          id: z.number(),
          email: z.string(),
          fullName: z.string()
        })
      }
    }
  }
};
```

### OpenAPI Documentation
Automatic API documentation generation via Fastify Swagger:

```typescript
fastify.register(fastifySwagger, {
  openapi: {
    info: { title: "Markit API", version: "1.0.0" },
    components: {
      securitySchemes: {
        bearerAuth: {
          type: "http",
          scheme: "bearer",
          bearerFormat: "JWT"
        }
      }
    }
  }
});
```

### Response Patterns
Consistent response structure across all endpoints:

```typescript
// Success response
return reply.status(200).send({
  data: result,
  message: "Operation successful"
});

// Error response (handled by global error handler)
throw new APIError(
  "Resource not found",
  "Not Found",
  StatusCodes.NotFound
);
```

---

## Authentication & Authorization

### JWT Implementation
JWT-based authentication with role-based authorization:

```typescript
// JWT configuration
fastify.register(fastifyJwt, {
  secret: env.JWT_SECRET
});

// Authentication hook
fastify.decorate("authenticate", async (request, reply) => {
  await request.jwtVerify();
  if (!request.user) {
    throw new APIError("Invalid token", "Unauthorized", 401);
  }
});
```

### Role-Based Access Control
Three-tier role system:

```typescript
enum Role {
  User = "user",      // Regular users creating briefs
  Expert = "expert",  // Experts reviewing and editing strategies
  Admin = "admin"     // System administrators
}

// Expert-only access
fastify.decorate("isExpert", async (request, reply) => {
  await request.jwtVerify();
  if (request.user.role !== Role.Expert) {
    throw new APIError("Expert access required", "Forbidden", 403);
  }
});
```

### Security Features
- **Password Hashing**: bcrypt with 12 rounds
- **Email Verification**: Token-based email verification system
- **Password Reset**: Secure token-based password reset flow
- **Rate Limiting**: 100 requests per minute per IP
- **CORS Configuration**: Configurable origin allowlist

---

## External Integrations

### OpenAI Integration
AI-powered marketing strategy generation:

```typescript
import { openai } from "@ai-sdk/openai";

export const model = openai("gpt-4o-mini-2024-07-18");

// Strategy generation
const { text } = await generateText({
  model,
  system: "You are an expert marketing strategist...",
  prompt: buildPromptFromBrief(brief)
});
```

### Email Service (Resend)
Transactional email delivery:

```typescript
import { Resend } from "resend";

export const resend = new Resend(env.RESEND_API_KEY);

// Email verification
await resend.emails.send({
  from: "noreply@markit.com",
  to: user.email,
  subject: "Verify your email",
  html: verificationTemplate
});
```

### PDF Generation
Marketing strategy document generation:

```typescript
import { mdToPdf } from 'md-to-pdf';

// Convert strategy to PDF
const pdf = await mdToPdf(
  { content: strategyMarkdown },
  { format: 'A4', margin: '20mm' }
);
```

---

## Error Handling

### Global Error Handler
Centralized error handling with proper logging and user-friendly responses:

```typescript
export const errorHandler = (
  error: Error | FastifyError | APIError,
  request: FastifyRequest,
  reply: FastifyReply
) => {
  request.log.error(error);

  // Zod validation errors
  if (hasZodFastifySchemaValidationErrors(error)) {
    return reply.code(400).send({
      error: "Validation Error",
      issues: error.validation.map(issue => ({
        field: issue.instancePath,
        message: issue.message
      }))
    });
  }

  // Custom API errors
  if (error instanceof APIError) {
    return reply.status(error.statusCode).send({
      error: error.error,
      message: error.message,
      statusCode: error.statusCode
    });
  }

  // Fallback for unexpected errors
  return reply.status(500).send({
    error: "Internal Server Error",
    message: "An unexpected error occurred"
  });
};
```

### Error Categories
- **Validation Errors**: Schema validation failures (400)
- **Authentication Errors**: Invalid or missing tokens (401)
- **Authorization Errors**: Insufficient permissions (403)
- **Not Found Errors**: Resource not found (404)
- **Business Logic Errors**: Domain-specific errors (400-409)
- **External Service Errors**: Third-party service failures (502-504)

---

## Testing Strategy

### Testing Framework
Node.js built-in test runner with Fastify test utilities:

```typescript
import { test } from 'node:test';
import { build } from '../helper';

test('authentication flow', async (t) => {
  const app = await build(t);
  
  const signUpResponse = await app.inject({
    method: 'POST',
    url: '/auth/signup',
    payload: { email: 'test@example.com', password: 'password123' }
  });
  
  assert.equal(signUpResponse.statusCode, 201);
});
```

### Test Categories
- **Unit Tests**: Service layer logic, utility functions
- **Integration Tests**: API endpoints with database
- **Plugin Tests**: Fastify plugin functionality
- **Error Handling Tests**: Error scenarios and edge cases

### Test Utilities
```typescript
// Test helper for app initialization
async function build(t: TestContext) {
  const app = await helper.build(argv, config());
  t.after(() => void app.close());
  return app;
}
```

### Coverage Configuration
- **Tool**: c8 coverage reporter
- **Target**: Comprehensive coverage of service layer and API endpoints
- **CI Integration**: Automated testing in deployment pipeline

---

## Deployment & Environment

### Environment Configuration
Type-safe environment variable validation:

```typescript
export const envSchema = z.object({
  OPENAI_API_KEY: z.string(),
  DATABASE_URL: z.string(),
  JWT_SECRET: z.string(),
  RESEND_API_KEY: z.string(),
  FRONTEND_URL: z.string()
});

export const env = envSchema.parse(process.env);
```

### Build Process
```json
{
  "scripts": {
    "build:ts": "npx prisma generate && tsc",
    "dev": "npx prisma generate && npm run build:ts && concurrently \"npm:watch:ts\" \"npm:dev:start\"",
    "start": "node -r ./tsconfig-paths-bootstrap.js ./node_modules/fastify-cli/cli.js start -l info dist/app.js"
  }
}
```

### Database Migrations
Prisma-managed database schema evolution:

```bash
# Generate migration
npx prisma migrate dev --name migration_name

# Deploy to production
npx prisma migrate deploy

# Reset development database
npx prisma migrate reset
```

### Production Considerations
- **Process Management**: PM2 or similar for process management
- **Reverse Proxy**: Nginx for load balancing and SSL termination
- **Database**: PostgreSQL with connection pooling
- **Monitoring**: Application performance monitoring and logging
- **Backup**: Automated database backups

---

## Performance & Scalability

### Fastify Performance Features
- **High Performance**: Built for speed with minimal overhead
- **Async/Await**: Non-blocking I/O operations throughout
- **Schema Compilation**: Fast JSON schema validation and serialization
- **Plugin Architecture**: Lazy loading and efficient memory usage

### Database Optimization
```typescript
// Efficient queries with proper includes
async getFullBrief(briefId: number) {
  return await this.db.brief.findUnique({
    where: { id: briefId },
    include: {
      businessInformation: true,
      marketingGoal: { include: { marketingObjectives: true } },
      targetAudience: {
        include: {
          customerBusiness: true,
          customerIndividual: true,
          customerBoth: true
        }
      },
      aiStrategy: {
        include: {
          blocks: {
            include: { sections: true },
            orderBy: { order: 'asc' }
          }
        }
      }
    }
  });
}
```

### Scalability Patterns
- **Modular Monolith**: Easy extraction to microservices
- **Database Sharding**: User-based data partitioning potential
- **Caching Strategy**: Redis integration for frequently accessed data
- **Load Balancing**: Stateless design enables horizontal scaling

### Rate Limiting
```typescript
await fastify.register(import("@fastify/rate-limit"), {
  max: 100,
  timeWindow: "1 minute"
});
```

---

## Security Considerations

### Data Protection
- **Password Security**: bcrypt hashing with 12 rounds
- **JWT Security**: Secure secret management and token expiration
- **Input Validation**: Comprehensive Zod schema validation
- **SQL Injection Prevention**: Prisma ORM parameterized queries

### API Security
- **CORS Configuration**: Restricted origin access
- **Rate Limiting**: DDoS protection and abuse prevention
- **Authentication Required**: Protected endpoints with JWT verification
- **Role-Based Access**: Granular permission system

### Environment Security
- **Secret Management**: Environment variable validation
- **Database Security**: Connection string protection
- **API Key Management**: Secure storage of third-party credentials

### Audit Trail
- **Request Logging**: Comprehensive request/response logging
- **Error Tracking**: Detailed error logging with stack traces
- **User Activity**: Authentication and authorization logging

---

## Development Workflow

### Development Setup
```bash
# Install dependencies
npm install

# Set up environment
cp .env.example .env

# Initialize database
npx prisma migrate dev
npx prisma db seed

# Start development server
npm run dev
```

### Code Organization Standards
- **TypeScript**: Strict type checking enabled
- **Module Structure**: Consistent controller/service/validation pattern
- **Path Aliases**: Clean imports with `@/` prefix
- **Error Handling**: Consistent APIError usage
- **Schema Validation**: Zod schemas for all API contracts

### Development Tools
- **Hot Reload**: File watching with automatic restart
- **Type Checking**: Real-time TypeScript compilation
- **Database Tools**: Prisma Studio for database inspection
- **API Documentation**: Swagger UI at `/documentation`

### Git Workflow
- **Feature Branches**: Isolated development in feature branches
- **Migration Management**: Database migrations in version control
- **Schema Evolution**: Coordinated schema and code changes
- **Testing Requirements**: Comprehensive test coverage for new features

---

## API Documentation

### Swagger Integration
The server automatically generates OpenAPI 3.0 documentation accessible at `/documentation` endpoint. The documentation includes:

- **Authentication Schemes**: JWT bearer token authentication
- **Request/Response Schemas**: Auto-generated from Zod schemas
- **Error Responses**: Standardized error response formats
- **Interactive Testing**: Built-in API testing interface

### Example API Endpoints

#### Authentication
```
POST /auth/signup          # User registration
POST /auth/signin          # User login
POST /auth/verify-email    # Email verification
PUT  /auth/change-password # Password reset
```

#### Brief Management
```
POST /brief/business-information  # Business info step
POST /brief/marketing-goals      # Marketing goals step
POST /brief/target-audience      # Target audience step
POST /brief/marketing-resources  # Resources step
POST /brief/competitors          # Competitor analysis step
```

#### Strategy Management
```
GET  /strategy              # List strategies (expert)
POST /strategy              # Generate new strategy
PUT  /strategy/:id          # Update strategy (expert)
GET  /strategy/download/:id # Download PDF
POST /strategy/send/:id     # Email strategy
```

---

<!-- DOCUMENT_METADATA_END
This server architecture documentation has been optimized for LLM parsing and embedding generation with the following enhancements:
- Added comprehensive document metadata and keywords for better searchability
- Enhanced section markers (SECTION_START/SECTION_END) for improved document chunking
- Structured information with detailed explanations and business context for each architectural component
- Added explicit purpose, implementation, and benefits for each technology and pattern
- Included comprehensive technology descriptions with use cases and integration details
- Enhanced architectural pattern explanations with implementation details and benefits
- Structured module descriptions with clear responsibilities and relationships
- Added detailed context for when and why specific patterns and technologies are used
- Improved code example explanations with context and business purpose
- Optimized for semantic search and knowledge extraction by AI systems
- Enhanced server architecture understanding with modular design principles
- Improved readability and parsing for automated documentation systems
- Added comprehensive API documentation with clear endpoint categorization
- Structured security and deployment information with practical implementation guidance
-->
