# Tech Stack & Best Practices Guide

<!-- DOCUMENT_METADATA
Document Type: Technical Stack and Development Best Practices Guide
Project: Markit Backend Server Application
Framework: Node.js with Fastify and TypeScript
Architecture Pattern: Modular Monolith with Plugin System
Database: PostgreSQL with Prisma ORM
Purpose: Comprehensive guide to technology stack decisions, development best practices, and production-ready implementation standards
Last Updated: 2024
-->

<!-- KEYWORDS: Tech-Stack, Best-Practices, Node.js, Fastify, TypeScript, PostgreSQL, Prisma, Development-Standards, Code-Quality, Security, Performance, Testing, Deployment -->

## Table of Contents

1. [Technology Stack Overview](#technology-stack-overview) - Complete technology stack overview and architectural philosophy
2. [Core Technologies](#core-technologies) - Runtime, framework, language, and database technologies
3. [Development Tools](#development-tools) - Build tools, testing frameworks, and developer experience tools
4. [Best Practices](#best-practices) - Project organization, plugin development, and service architecture patterns
5. [Code Standards](#code-standards) - Naming conventions, file organization, and function design standards
6. [Security Best Practices](#security-best-practices) - Authentication, authorization, data protection, and security measures
7. [Performance Optimization](#performance-optimization) - Database optimization, caching strategies, and response optimization
8. [Testing Guidelines](#testing-guidelines) - Test structure, patterns, and data management for comprehensive testing
9. [Database Best Practices](#database-best-practices) - Schema design, migration strategies, and query optimization
10. [API Design Guidelines](#api-design-guidelines) - RESTful design, response formats, and versioning strategies
11. [Error Handling Standards](#error-handling-standards) - Error classification, middleware, and logging standards
12. [Deployment Best Practices](#deployment-best-practices) - Environment configuration, health checks, and production optimization

---

## Technology Stack Overview

<!-- SECTION_START: Technology Stack Philosophy and Architecture -->
**Context**: The Markit server is built using modern, production-ready technologies that prioritize **type safety**, **performance**, and **developer experience**. The stack is designed for **scalability** and **maintainability** while providing excellent tooling support for team collaboration and rapid development.

**Technical Foundation**: The technology stack emphasizes compile-time safety, runtime validation, and production-grade performance while maintaining developer productivity and code maintainability through modern tooling and best practices.

### Architecture Philosophy

**Type-First Development Approach**
- **Implementation**: TypeScript throughout with strict typing configuration enabled
- **Benefits**: Compile-time error detection, excellent IDE support, self-documenting code
- **Impact**: Reduced runtime errors, improved developer experience, enhanced code quality
- **Tools**: TypeScript compiler with strict mode, ESLint TypeScript rules, Prettier formatting

**Schema-Driven Design Methodology**
- **Implementation**: Zod schemas for comprehensive validation and automatic documentation generation
- **Benefits**: Runtime validation, type inference, consistent API contracts, automatic documentation
- **Impact**: Reduced validation errors, improved API reliability, enhanced developer experience
- **Integration**: Fastify schema validation, OpenAPI generation, type-safe request/response handling

**Plugin-Based Architecture Pattern**
- **Implementation**: Fastify plugin system for modular, testable, and maintainable code organization
- **Benefits**: Separation of concerns, easy testing, simplified maintenance, potential microservices extraction
- **Impact**: Improved code organization, better team collaboration, enhanced scalability potential
- **Structure**: Domain-driven modules, clear boundaries, dependency injection, lifecycle management

**Database-First Development Strategy**
- **Implementation**: Prisma ORM for type-safe database operations with schema-driven development
- **Benefits**: Type safety at database level, automatic migrations, optimized query generation
- **Impact**: Reliable data persistence, simplified database operations, reduced SQL errors
- **Features**: Schema evolution, type generation, query optimization, migration management

**API-First Design Approach**
- **Implementation**: OpenAPI documentation with automatic generation from Zod schemas
- **Benefits**: Clear API contracts, interactive documentation, client generation capabilities
- **Impact**: Improved team collaboration, easier integration, comprehensive API testing
- **Tools**: Fastify Swagger integration, interactive documentation, schema validation
<!-- SECTION_END: Technology Stack Philosophy and Architecture -->

---

## Core Technologies

<!-- SECTION_START: Core Runtime and Framework Technologies -->
**Overview**: The core technology foundation consists of carefully selected runtime, framework, and language technologies that provide high performance, type safety, and excellent developer experience while maintaining production-grade reliability.

### 1. Runtime & Framework Technologies

#### Node.js - JavaScript Runtime Environment
- **Version**: Latest LTS (22.x recommended) for stability and long-term support
- **Purpose**: High-performance JavaScript runtime providing the foundation for server-side execution
- **Key Benefits**: 
  - High-performance asynchronous I/O operations ideal for API servers and concurrent request handling
  - Excellent ecosystem with comprehensive package availability through npm
  - Strong TypeScript support with native ES modules and modern JavaScript features
  - Non-blocking event-driven architecture perfect for I/O-intensive applications
- **Use Cases**: Server application runtime, package management, build processes, development tooling
- **Performance**: Single-threaded event loop with worker threads for CPU-intensive tasks

#### Fastify - High-Performance Web Framework
```typescript
// app.ts - Framework configuration
import { FastifyPluginAsync, FastifyServerOptions } from "fastify";

const app: FastifyPluginAsync<AppOptions> = async (fastify, opts) => {
  // High-performance request handling
  fastify.setValidatorCompiler(validatorCompiler);
  fastify.setSerializerCompiler(serializerCompiler);
  
  // Type-safe plugin system
  fastify.withTypeProvider<ZodTypeProvider>();
};
```

**Why Fastify for Markit Server?**
- **Performance**: Up to 30% faster than Express with optimized request handling and minimal overhead
- **Type Safety**: First-class TypeScript support with comprehensive type inference and plugin typing
- **Plugin Architecture**: Modular and testable design enabling domain-driven development and easy maintenance
- **Schema Validation**: Built-in JSON schema support with automatic validation and serialization
- **Async/Await**: Native promise support throughout the framework for modern asynchronous programming
- **Production Ready**: Built-in logging, error handling, and performance monitoring capabilities
- **Ecosystem**: Rich plugin ecosystem with official and community-maintained extensions

### 2. Language & Type System Technologies

#### TypeScript - Static Type System and Language Enhancement
- **Purpose**: Superset of JavaScript providing static type checking, enhanced developer experience, and enterprise-grade development capabilities
- **Version**: Latest stable version with strict configuration enabled for maximum type safety
- **Configuration Strategy**: Comprehensive type coverage with strict null checks, no implicit any, and enhanced error checking

```json
// tsconfig.json - Strict configuration optimized for server development
{
  "extends": "fastify-tsconfig",
  "compilerOptions": {
    "strict": true,                    // Enable all strict type checking options
    "noImplicitAny": true,            // Error on expressions and declarations with implied 'any' type
    "strictNullChecks": true,         // Enable strict null checks for better null safety
    "outDir": "dist",                 // Output directory for compiled JavaScript
    "sourceMap": true,                // Generate source maps for debugging
    "baseUrl": ".",                   // Base directory for module resolution
    "paths": {                        // Path mapping for clean imports
      "@/*": ["src/*"],
      "@utils/*": ["src/utils/*"],
      "@config/*": ["src/config/*"],
      "@constants/*": ["src/constants/*"],
      "@modules/*": ["src/modules/*"],
      "@db/*": ["src/db/*"],
      "@generated/*": ["generated/*"]
    }
  }
}
```

**Key Benefits for Markit Development**:
- **Compile-time Safety**: Catch type errors, null reference errors, and logic errors before runtime execution
- **Enhanced IDE Support**: Comprehensive IntelliSense, autocomplete, and real-time error detection in development
- **Safe Refactoring**: Confident code transformations with compiler-verified changes across the codebase
- **Living Documentation**: Types serve as always-up-to-date documentation that can't become stale
- **Team Collaboration**: Shared understanding through explicit type contracts and interfaces
- **Reduced Runtime Errors**: Significant reduction in production bugs through compile-time validation

#### Zod - TypeScript-First Schema Validation Library
- **Purpose**: Runtime validation library with TypeScript type inference for comprehensive data validation
- **Integration**: Seamless TypeScript integration with automatic type generation from schemas
- **Features**: Custom validators, error handling, type coercion, nested object validation
- **Benefits**: Type safety, runtime validation, excellent TypeScript integration, clear error messages

```typescript
// Comprehensive schema validation with type inference
export const authSchema = {
  signUp: {
    body: z.object({
      email: z.string()
        .email("Invalid email format")
        .toLowerCase()                           // Automatic data transformation
        .trim(),                                // Input sanitization
      fullName: z.string()
        .min(2, "Name must be at least 2 characters")
        .max(100, "Name must be less than 100 characters")
        .trim(),
      password: z.string()
        .min(8, "Password must be at least 8 characters")
        .regex(/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)/, "Password must contain uppercase, lowercase, and number")
    }),
    response: {
      201: z.object({
        id: z.number(),
        email: z.string(),
        fullName: z.string(),
        role: z.enum(["user", "expert", "admin"])
      })
    }
  }
};

// Type inference from schema
type SignUpRequest = z.infer<typeof authSchema.signUp.body>;
type SignUpResponse = z.infer<typeof authSchema.signUp.response[201]>;
```

**Zod Advantages for API Development**:
- **Type Inference**: Automatic TypeScript types generated from validation schemas
- **Runtime Safety**: Comprehensive validation of incoming data with detailed error messages
- **Data Transformation**: Built-in data coercion, sanitization, and transformation capabilities
- **Error Handling**: Structured error responses with field-specific validation messages
- **Documentation**: Schemas serve as API contract documentation with validation rules
<!-- SECTION_END: Core Runtime and Framework Technologies -->

### 3. Database Layer Technologies

<!-- SECTION_START: Database and Data Management Technologies -->
**Overview**: The database layer provides reliable, performant, and type-safe data persistence using PostgreSQL as the primary database with Prisma ORM for modern database operations and schema management.

#### PostgreSQL - Production-Grade Relational Database
- **Version**: 15+ recommended for advanced features and performance improvements
- **Purpose**: Robust, ACID-compliant relational database system for reliable data persistence and complex query operations
- **Architecture Role**: Primary data store for user accounts, marketing briefs, AI strategies, and application metadata

**Key Features Utilized**:
- **JSONB Storage**: Flexible semi-structured data storage for dynamic content like AI strategy blocks and user preferences
- **Advanced Constraints**: Data integrity enforcement through foreign keys, check constraints, and unique indexes
- **Performance Indexes**: Strategic indexing for query optimization including composite indexes for complex queries
- **Transaction Support**: ACID compliance for data consistency across complex operations
- **Full-Text Search**: Built-in search capabilities for content discovery and filtering
- **JSON Operations**: Native JSON querying and manipulation for flexible data structures

**Production Benefits**:
- **Reliability**: ACID transactions ensure data consistency and integrity
- **Scalability**: Excellent performance with proper indexing and query optimization
- **Feature Richness**: Advanced SQL features, stored procedures, and extensive data types
- **Ecosystem**: Mature tooling, monitoring, and operational support

#### Prisma ORM - Modern Database Toolkit
```prisma
// schema.prisma - Type-safe database schema
generator client {
  provider = "prisma-client-js"
  output   = "../generated/prisma"
}

model User {
  id       Int     @id @default(autoincrement())
  email    String  @unique
  fullName String
  role     Role    @default(user)
  briefs   Brief[]
}
```

**Prisma Advantages for Markit Development**:
- **Type Safety**: Auto-generated TypeScript types from database schema ensuring compile-time safety
- **Migration Management**: Automated schema evolution with version control and rollback capabilities
- **Query Builder**: Intuitive and type-safe query API with IntelliSense support and relation loading
- **Performance**: Optimized query generation with automatic join optimization and query analysis
- **Developer Experience**: Prisma Studio for database browsing, schema visualization, and data management
- **Database Introspection**: Automatic schema discovery and reverse engineering from existing databases

**Prisma Integration Benefits**:
- **Schema-First Development**: Database schema as single source of truth for data modeling
- **Automatic Client Generation**: TypeScript client with full type inference and autocomplete
- **Relation Management**: Intuitive handling of complex relationships with automatic join generation
- **Migration Workflow**: Seamless development-to-production schema deployment pipeline
- **Error Prevention**: Compile-time validation of database operations and schema compliance
<!-- SECTION_END: Database and Data Management Technologies -->

---

## Development Tools

<!-- SECTION_START: Development and Build Tools -->
**Overview**: The development toolchain emphasizes developer productivity, code quality, and efficient workflows through modern build tools, testing frameworks, and documentation generation systems.

### 1. Build & Development Tools

#### TypeScript Compiler - Code Compilation and Type Checking
```json
// package.json - Build scripts
{
  "scripts": {
    "build:ts": "npx prisma generate && tsc",
    "watch:ts": "tsc -w",
    "dev": "npx prisma generate && npm run build:ts && concurrently \"npm:watch:ts\" \"npm:dev:start\""
  }
}
```

#### Concurrently
- **Purpose**: Run multiple development processes
- **Usage**: TypeScript compilation + server restart
- **Benefits**: Streamlined development workflow

```bash
# Development with hot reload
npm run dev
# Runs: Prisma generation → TypeScript compilation → Server start
```

#### TSConfig Paths
```javascript
// tsconfig-paths-bootstrap.js - Module resolution
const tsConfigPaths = require("tsconfig-paths");
const cleanup = tsConfigPaths.register({
  baseUrl: "./dist",
  paths: transformPaths(tsConfig.compilerOptions.paths)
});
```

### 2. Testing Framework and Quality Assurance

#### Node.js Test Runner - Built-in Testing Framework
- **Purpose**: Native Node.js testing framework providing modern testing capabilities without external dependencies
- **Features**: Async/await support, test isolation, parallel execution, built-in assertions, TypeScript support
- **Benefits**: Zero-dependency testing, fast execution, modern API, seamless Node.js integration
- **Use Cases**: Unit testing, integration testing, API endpoint testing, service layer validation

```typescript
// test/example.test.ts - Modern testing with comprehensive coverage
import { test } from 'node:test';
import * as assert from 'node:assert';
import { build } from '../helper';

test('authentication flow with complete validation', async (t) => {
  const app = await build(t);
  
  // Test user registration
  const signUpResponse = await app.inject({
    method: 'POST',
    url: '/auth/signup',
    payload: {
      email: 'test@example.com',
      fullName: 'Test User',
      password: 'SecurePass123!'
    }
  });
  
  assert.equal(signUpResponse.statusCode, 201);
  
  const userData = signUpResponse.json();
  assert.ok(userData.id);
  assert.equal(userData.email, 'test@example.com');
  assert.equal(userData.role, 'user');
});

test('input validation error handling', async (t) => {
  const app = await build(t);
  
  const invalidResponse = await app.inject({
    method: 'POST',
    url: '/auth/signup',
    payload: {
      email: 'invalid-email',
      password: '123'  // Too short
    }
  });
  
  assert.equal(invalidResponse.statusCode, 400);
  const errorData = invalidResponse.json();
  assert.equal(errorData.error, 'Validation Error');
  assert.ok(errorData.issues.length > 0);
});
```

#### C8 Coverage
```json
// package.json - Coverage configuration
{
  "scripts": {
    "test": "npm run build:ts && tsc -p test/tsconfig.json && c8 node --test -r ts-node/register \"test/**/*.ts\""
  }
}
```

### 3. API Documentation and Developer Experience

#### Swagger/OpenAPI - Interactive API Documentation
- **Purpose**: Automatic API documentation generation with interactive testing capabilities
- **Integration**: Seamless integration with Fastify and Zod schemas for always-up-to-date documentation
- **Features**: Interactive UI, authentication support, request/response examples, schema validation
- **Benefits**: Reduced documentation maintenance, improved developer onboarding, comprehensive API testing

```typescript
// Comprehensive API documentation configuration
fastify.register(fastifySwagger, {
  openapi: {
    info: { 
      title: "Markit API", 
      version: "1.0.0",
      description: "Marketing strategy generation platform API",
      contact: {
        name: "Markit Team",
        email: "support@markit.com"
      }
    },
    servers: [
      {
        url: "http://localhost:3000",
        description: "Development server"
      },
      {
        url: "https://api.markit.com",
        description: "Production server"
      }
    ],
    components: {
      securitySchemes: {
        bearerAuth: {
          type: "http",
          scheme: "bearer",
          bearerFormat: "JWT",
          description: "JWT authorization token"
        }
      }
    },
    tags: [
      { name: "Authentication", description: "User authentication and authorization" },
      { name: "Brief Management", description: "Marketing brief creation and management" },
      { name: "Strategy Generation", description: "AI-powered marketing strategy operations" }
    ]
  },
  transform: jsonSchemaTransform,
  uiConfig: {
    docExpansion: 'list',
    deepLinking: true
  }
});

// Register Swagger UI
fastify.register(fastifySwaggerUI, {
  routePrefix: '/documentation',
  uiConfig: {
    docExpansion: 'list',
    deepLinking: true,
    defaultModelsExpandDepth: 2
  }
});
```

**Documentation Benefits**:
- **Always Current**: Auto-generated from code, preventing documentation drift
- **Interactive Testing**: Built-in API testing interface for development and debugging
- **Schema Validation**: Request/response validation directly in documentation
- **Developer Onboarding**: Comprehensive API exploration and learning tool
- **Client Generation**: OpenAPI spec enables automatic client library generation
<!-- SECTION_END: Development and Build Tools -->

### 4. Code Quality Tools

#### ESLint (Recommended)
```json
// .eslintrc.js - Code quality rules
module.exports = {
  extends: [
    '@typescript-eslint/recommended',
    'plugin:@typescript-eslint/recommended-requiring-type-checking'
  ],
  rules: {
    '@typescript-eslint/no-unused-vars': 'error',
    '@typescript-eslint/explicit-function-return-type': 'warn'
  }
};
```

#### Prettier (Recommended)
```json
// .prettierrc - Code formatting
{
  "semi": true,
  "trailingComma": "es5",
  "singleQuote": false,
  "printWidth": 80,
  "tabWidth": 2
}
```

---

## Best Practices

<!-- SECTION_START: Development Best Practices and Patterns -->
**Overview**: Best practices for the Markit server emphasize maintainable code organization, scalable architecture patterns, and efficient development workflows that support team collaboration and long-term project success.

### 1. Project Structure and Organization

#### Modular Organization Strategy
- **Purpose**: Clear separation of concerns with domain-driven module organization for maintainability and scalability
- **Benefits**: Independent development, easy testing, clear ownership boundaries, potential microservices extraction
- **Implementation**: Consistent module structure across all business domains with standardized patterns
```
src/
├── modules/              # Business logic modules
│   ├── auth/            # Authentication domain
│   │   ├── index.ts     # Plugin registration
│   │   ├── controller.ts # Request handlers
│   │   ├── service.ts   # Business logic
│   │   ├── validation.ts # Zod schemas
│   │   └── constants.ts # Module constants
│   └── brief/           # Brief management domain
├── plugins/             # Fastify plugins
├── routes/              # Route definitions
├── config/              # Configuration
├── utils/               # Shared utilities
└── constants/           # Global constants
```

**Guidelines**:
- **Single Responsibility**: Each module handles one domain
- **Clear Boundaries**: Minimal inter-module dependencies
- **Consistent Structure**: Same pattern across all modules
- **Self-Contained**: Modules can be independently tested

### 2. Plugin Development Patterns

#### Standard Plugin Architecture Pattern
- **Purpose**: Consistent plugin structure across all modules ensuring predictable development patterns and easy maintenance
- **Benefits**: Self-contained modules, clear dependency management, testable components, lifecycle management
- **Implementation**: Standardized plugin registration with service decoration and route organization

```typescript
// Comprehensive module plugin structure with full lifecycle management
const modulePlugin: FastifyPluginAsync = async (fastify, opts) => {
  // 1. Validate plugin options and configuration
  const pluginOptions = validatePluginOptions(opts);
  
  // 2. Decorate services with dependency injection
  fastify.decorate("moduleService", new ModuleService(
    fastify.prisma,
    fastify.log,
    pluginOptions.config
  ));
  
  // 3. Decorate controllers with service dependencies
  fastify.decorate("moduleController", 
    new ModuleController(
      fastify.moduleService,
      fastify.log
    )
  );
  
  // 4. Add lifecycle hooks for request processing
  fastify.addHook("onRequest", async (request, reply) => {
    request.log.info(`Processing ${request.method} ${request.url}`);
  });
  
  // 5. Add authentication hooks for protected routes
  fastify.addHook("onRequest", fastify.authenticate);
  
  // 6. Register routes with comprehensive schema validation
  fastify.get("/route", {
    schema: moduleSchema.getRoute,
    onRequest: [fastify.authenticate, fastify.authorize('user')],
    handler: fastify.moduleController.getHandler
  });
  
  fastify.post("/route", {
    schema: moduleSchema.createRoute,
    onRequest: [fastify.authenticate, fastify.authorize('user')],
    handler: fastify.moduleController.createHandler
  });
  
  // 7. Add cleanup hooks for resource management
  fastify.addHook("onClose", async (instance, done) => {
    await fastify.moduleService.cleanup();
    done();
  });
};

export default modulePlugin;
```

**Plugin Development Best Practices**:
- **Encapsulation**: Each plugin is completely self-contained with clear boundaries and minimal external dependencies
- **Dependency Injection**: Services and controllers injected via Fastify decorators for easy testing and mocking
- **Type Safety**: Full TypeScript support with comprehensive type checking and inference throughout the plugin
- **Testing Isolation**: Easy to mock dependencies and test individual components in isolation
- **Lifecycle Management**: Proper setup and cleanup through Fastify hooks ensuring resource management
- **Error Handling**: Consistent error handling patterns with proper logging and user-friendly error responses

### 3. Service Layer Design

#### Service Class Pattern
```typescript
export class BriefService {
  constructor(private db: PrismaClient) {}

  async create(userId: number, data: BriefCreateData): Promise<Brief> {
    // Validation
    this.validateBriefData(data);
    
    // Business logic
    const brief = await this.db.brief.create({
      data: { userId, ...data },
      include: this.getDefaultIncludes()
    });
    
    // Post-processing
    await this.triggerBriefCreatedEvent(brief);
    
    return brief;
  }

  private validateBriefData(data: BriefCreateData): void {
    // Domain-specific validation
  }

  private getDefaultIncludes(): object {
    // Reusable include configuration
  }
}
```

**Principles**:
- **Single Responsibility**: One service per domain
- **Dependency Injection**: Database injected in constructor
- **Error Handling**: Domain-specific error types
- **Reusability**: Common patterns extracted to private methods

---

## Code Standards

### 1. Naming Conventions

#### Variables & Functions
```typescript
// Camel case for variables and functions
const userEmail = "user@example.com";
const calculateTotalPrice = (items: Item[]) => { };

// Descriptive names
const isUserAuthenticated = checkAuthentication(user);
const briefWithComponents = await getBriefWithAllComponents(briefId);
```

#### Classes & Interfaces
```typescript
// Pascal case for classes and interfaces
class AuthService { }
interface UserCreateData { }
type BriefStatus = "draft" | "completed";

// Descriptive and domain-specific
class MarketingStrategyGenerator { }
interface BriefComponentData { }
```

#### Constants & Enums
```typescript
// Upper snake case for constants
const JWT_SECRET_KEY = process.env.JWT_SECRET;
const MAX_BRIEF_COMPONENTS = 10;

// Pascal case for enums
enum UserRole {
  User = "user",
  Expert = "expert",
  Admin = "admin"
}
```

### 2. File Organization

#### Import Order
```typescript
// 1. Node.js built-ins
import { join } from "node:path";

// 2. External libraries
import { FastifyPluginAsync } from "fastify";
import { z } from "zod";

// 3. Internal imports (absolute paths)
import { AuthService } from "@modules/auth/service";
import { APIError } from "@utils/error-handler";

// 4. Relative imports
import { authRoutes } from "./constants";
import { authSchema } from "./validation";
```

#### Export Patterns
```typescript
// Named exports preferred
export { AuthService } from "./service";
export { AuthController } from "./controller";

// Default export for main module
export default authPlugin;

// Type-only exports when appropriate
export type { AuthData, LoginResponse } from "./types";
```

### 3. Function Design

#### Pure Functions
```typescript
// Pure function - no side effects
const calculateDiscountedPrice = (price: number, discount: number): number => {
  return price * (1 - discount / 100);
};

// Impure function - clearly named
const saveUserToDatabaseAndSendEmail = async (user: User): Promise<void> => {
  await database.user.create({ data: user });
  await emailService.sendWelcomeEmail(user.email);
};
```

#### Error Handling
```typescript
// Explicit error types
const getUserById = async (id: number): Promise<User> => {
  const user = await db.user.findUnique({ where: { id } });
  
  if (!user) {
    throw new APIError(
      `User with ID ${id} not found`,
      "User Not Found",
      StatusCodes.NotFound
    );
  }
  
  return user;
};
```

---

## Security Best Practices

### 1. Authentication & Authorization

#### JWT Implementation
```typescript
// Secure JWT configuration
fastify.register(fastifyJwt, {
  secret: env.JWT_SECRET,
  sign: {
    expiresIn: "7d",
    issuer: "markit-api"
  },
  verify: {
    issuer: "markit-api"
  }
});
```

#### Role-Based Access Control
```typescript
// Fine-grained permissions
const isExpert = async (request: FastifyRequest, reply: FastifyReply) => {
  await request.jwtVerify();
  
  if (request.user.role !== Role.Expert) {
    throw new APIError(
      "Expert access required",
      "Forbidden",
      StatusCodes.Forbidden
    );
  }
};

// Usage in routes
fastify.get("/expert-route", {
  onRequest: [fastify.isExpert]
}, handler);
```

### 2. Input Validation

#### Comprehensive Schemas
```typescript
// Strict validation with sanitization
const userRegistrationSchema = z.object({
  email: z.string()
    .email("Invalid email format")
    .toLowerCase()
    .trim(),
  
  password: z.string()
    .min(8, "Password must be at least 8 characters")
    .regex(/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)/, "Password must contain uppercase, lowercase, and number"),
  
  fullName: z.string()
    .min(2, "Name must be at least 2 characters")
    .max(100, "Name must be less than 100 characters")
    .trim()
});
```

### 3. Data Protection

#### Password Security
```typescript
// Secure password hashing
const hashPassword = async (password: string): Promise<string> => {
  const saltRounds = 12; // Higher rounds for better security
  return await bcrypt.hash(password, saltRounds);
};

// Secure comparison
const validatePassword = async (password: string, hash: string): Promise<boolean> => {
  return await bcrypt.compare(password, hash);
};
```

#### Environment Variables
```typescript
// Type-safe environment validation
export const envSchema = z.object({
  JWT_SECRET: z.string().min(32, "JWT secret must be at least 32 characters"),
  DATABASE_URL: z.string().url("Invalid database URL"),
  OPENAI_API_KEY: z.string().min(1, "OpenAI API key required"),
  RESEND_API_KEY: z.string().min(1, "Resend API key required")
});

export const env = envSchema.parse(process.env);
```

### 4. Rate Limiting & DDoS Protection

#### Progressive Rate Limiting
```typescript
// Basic rate limiting
await fastify.register(import("@fastify/rate-limit"), {
  max: 100,
  timeWindow: "1 minute",
  errorResponseBuilder: (request, context) => ({
    error: "Rate Limit Exceeded",
    message: `You can only make ${context.max} requests per ${context.timeWindow}`,
    statusCode: 429
  })
});

// Stricter limits for auth endpoints
fastify.register(async (fastify) => {
  await fastify.register(import("@fastify/rate-limit"), {
    max: 5,
    timeWindow: "1 minute"
  });
  
  fastify.register(authRoutes);
});
```

---

## Performance Optimization

### 1. Database Optimization

#### Efficient Queries
```typescript
// Optimized includes
const getBriefWithComponents = async (briefId: number) => {
  return await db.brief.findUnique({
    where: { id: briefId },
    include: {
      businessInformation: true,
      marketingGoal: {
        include: { marketingObjectives: true }
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
};

// Avoid N+1 queries
const getUsersWithBriefs = async () => {
  return await db.user.findMany({
    include: {
      briefs: {
        include: { aiStrategy: true }
      }
    }
  });
};
```

#### Query Optimization
```typescript
// Pagination for large datasets
const getPaginatedUsers = async (page: number, limit: number) => {
  const skip = (page - 1) * limit;
  
  const [users, total] = await Promise.all([
    db.user.findMany({
      skip,
      take: limit,
      orderBy: { createdAt: 'desc' }
    }),
    db.user.count()
  ]);
  
  return {
    users,
    pagination: {
      page,
      limit,
      total,
      pages: Math.ceil(total / limit)
    }
  };
};
```

### 2. Caching Strategies

#### Redis Integration (Recommended)
```typescript
// Cache implementation example
class CacheService {
  constructor(private redis: Redis) {}
  
  async getOrSet<T>(
    key: string,
    getter: () => Promise<T>,
    ttl: number = 300
  ): Promise<T> {
    const cached = await this.redis.get(key);
    
    if (cached) {
      return JSON.parse(cached);
    }
    
    const data = await getter();
    await this.redis.setex(key, ttl, JSON.stringify(data));
    
    return data;
  }
}

// Usage in services
const getDefaultOptions = async () => {
  return cacheService.getOrSet(
    'default-options',
    () => db.businessModel.findMany({ where: { userGenerated: false } }),
    3600 // 1 hour TTL
  );
};
```

### 3. Response Optimization

#### JSON Schema Serialization
```typescript
// Fast JSON serialization
const userResponseSchema = {
  type: 'object',
  properties: {
    id: { type: 'number' },
    email: { type: 'string' },
    fullName: { type: 'string' },
    role: { type: 'string' }
  }
};

// Register schema for fast serialization
fastify.addSchema({
  $id: 'user',
  ...userResponseSchema
});

// Use in route response
const userRouteSchema = {
  response: {
    200: { $ref: 'user' }
  }
};
```

---

## Testing Guidelines

### 1. Test Structure

#### Test Organization
```
test/
├── unit/              # Unit tests
│   ├── services/      # Service layer tests
│   ├── utils/         # Utility function tests
│   └── validators/    # Schema validation tests
├── integration/       # Integration tests
│   ├── routes/        # API endpoint tests
│   └── database/      # Database operation tests
└── e2e/              # End-to-end tests
    └── workflows/     # Complete user workflows
```

#### Test Naming
```typescript
// Descriptive test names
test('AuthService.signUp should create user and send verification email', async (t) => {
  // Test implementation
});

test('AuthService.signUp should throw error for duplicate email', async (t) => {
  // Test implementation
});

test('GET /auth/verify-email should verify user with valid token', async (t) => {
  // Test implementation
});
```

### 2. Testing Patterns

#### Service Testing
```typescript
// Service layer unit test
test('BriefService.create should validate and save brief', async (t) => {
  const mockDb = createMockPrismaClient();
  const briefService = new BriefService(mockDb);
  
  const briefData = {
    businessInformationId: 1,
    marketingGoalId: 1
  };
  
  const result = await briefService.create(1, briefData);
  
  assert.ok(result.id);
  assert.equal(result.userId, 1);
  assert.ok(mockDb.brief.create.calledOnce);
});
```

#### API Testing
```typescript
// Integration test with test app
test('POST /brief should create brief for authenticated user', async (t) => {
  const app = await build(t);
  
  // Create and authenticate user
  const { token } = await createTestUser(app);
  
  const response = await app.inject({
    method: 'POST',
    url: '/brief',
    headers: {
      authorization: `Bearer ${token}`
    },
    payload: validBriefData
  });
  
  assert.equal(response.statusCode, 201);
  assert.ok(response.json().id);
});
```

### 3. Test Data Management

#### Factory Pattern
```typescript
// Test data factories
export class TestDataFactory {
  static createUser(overrides: Partial<User> = {}): User {
    return {
      id: 1,
      email: 'test@example.com',
      fullName: 'Test User',
      role: Role.User,
      verified: true,
      ...overrides
    };
  }
  
  static createBrief(overrides: Partial<Brief> = {}): Brief {
    return {
      id: 1,
      userId: 1,
      businessInformationId: 1,
      createdAt: new Date(),
      ...overrides
    };
  }
}
```

---

## Database Best Practices

### 1. Schema Design

#### Naming Conventions
```prisma
// Clear, consistent naming
model User {
  id        Int      @id @default(autoincrement()) @map("id")
  email     String   @unique @map("email")
  fullName  String   @map("full_name")
  createdAt DateTime @default(now()) @map("created_at")
  
  @@map("user")
}

// Relationship naming
model Brief {
  userId Int  @map("user_id")
  user   User @relation(fields: [userId], references: [id])
}
```

#### Index Strategy
```prisma
model User {
  email String @unique @map("email") // Automatic index
  
  @@index([createdAt]) // Query optimization
  @@index([role, verified]) // Composite index
}

model Brief {
  userId Int
  status String
  
  @@index([userId, status]) // Common query pattern
}
```

### 2. Migration Best Practices

#### Safe Migrations
```sql
-- Add column with default value
ALTER TABLE "user" ADD COLUMN "tier" "Tier" NOT NULL DEFAULT 'one';

-- Add index concurrently (PostgreSQL)
CREATE INDEX CONCURRENTLY "idx_user_email_verified" ON "user" ("email", "verified");

-- Drop column in separate migration
ALTER TABLE "user" DROP COLUMN "old_column";
```

#### Migration Testing
```bash
# Test migration on copy of production data
npx prisma migrate dev --name test_migration

# Verify data integrity
npx prisma db seed

# Run application tests
npm test
```

### 3. Query Optimization

#### Efficient Patterns
```typescript
// Use select for specific fields
const getBasicUserInfo = async (id: number) => {
  return await db.user.findUnique({
    where: { id },
    select: {
      id: true,
      email: true,
      fullName: true,
      role: true
    }
  });
};

// Batch operations
const createMultipleBriefs = async (briefsData: BriefData[]) => {
  return await db.brief.createMany({
    data: briefsData,
    skipDuplicates: true
  });
};

// Transaction for consistency
const transferBriefOwnership = async (briefId: number, newUserId: number) => {
  return await db.$transaction(async (tx) => {
    const brief = await tx.brief.update({
      where: { id: briefId },
      data: { userId: newUserId }
    });
    
    await tx.auditLog.create({
      data: {
        action: 'BRIEF_TRANSFERRED',
        briefId,
        userId: newUserId
      }
    });
    
    return brief;
  });
};
```

---

## API Design Guidelines

### 1. RESTful Design

#### Resource Naming
```typescript
// Good: Noun-based resource names
GET    /briefs              // Get all briefs
POST   /briefs              // Create brief
GET    /briefs/:id          // Get specific brief
PUT    /briefs/:id          // Update brief
DELETE /briefs/:id          // Delete brief

// Nested resources
GET    /briefs/:id/strategy     // Get brief's strategy
POST   /strategies/:id/send     // Send strategy (action)
```

#### Status Codes
```typescript
// Consistent status code usage
const responses = {
  // Success
  200: 'OK - Resource retrieved/updated',
  201: 'Created - Resource created',
  204: 'No Content - Resource deleted',
  
  // Client errors
  400: 'Bad Request - Invalid input',
  401: 'Unauthorized - Authentication required',
  403: 'Forbidden - Insufficient permissions',
  404: 'Not Found - Resource not found',
  409: 'Conflict - Resource already exists',
  
  // Server errors
  500: 'Internal Server Error - Unexpected error',
  502: 'Bad Gateway - External service error'
};
```

### 2. Response Formats

#### Consistent Structure
```typescript
// Success response
interface SuccessResponse<T> {
  data: T;
  message?: string;
  meta?: {
    pagination?: PaginationMeta;
    total?: number;
  };
}

// Error response
interface ErrorResponse {
  error: string;
  message: string;
  statusCode: number;
  issues?: ValidationIssue[];
}

// Implementation
const sendSuccess = <T>(reply: FastifyReply, data: T, statusCode = 200) => {
  return reply.status(statusCode).send({
    data,
    message: 'Operation successful'
  });
};
```

### 3. Versioning Strategy

#### URL Versioning
```typescript
// Version in URL
fastify.register(async (fastify) => {
  fastify.addHook('onRequest', async (request) => {
    request.headers['api-version'] = 'v1';
  });
  
  // Register v1 routes
  fastify.register(v1Routes, { prefix: '/api/v1' });
});

// Header versioning (alternative)
fastify.addHook('onRequest', async (request, reply) => {
  const version = request.headers['api-version'] || 'v1';
  request.apiVersion = version;
});
```

---

## Error Handling Standards

### 1. Error Classification

#### Error Hierarchy
```typescript
// Base error class
export class APIError extends Error {
  constructor(
    message: string,
    public error: string,
    public statusCode: number,
    public context?: any
  ) {
    super(message);
    this.name = this.constructor.name;
    Error.captureStackTrace(this, this.constructor);
  }
}

// Specific error types
export class ValidationError extends APIError {
  constructor(message: string, issues: ValidationIssue[]) {
    super(message, 'Validation Error', 400, { issues });
  }
}

export class NotFoundError extends APIError {
  constructor(resource: string, id: string | number) {
    super(
      `${resource} with ID ${id} not found`,
      'Not Found',
      404,
      { resource, id }
    );
  }
}
```

### 2. Error Handling Middleware

#### Global Error Handler
```typescript
export const errorHandler = (
  error: Error | FastifyError | APIError,
  request: FastifyRequest,
  reply: FastifyReply
) => {
  // Log error with context
  request.log.error({
    error: error.message,
    stack: error.stack,
    url: request.url,
    method: request.method,
    userId: request.user?.id
  });

  // Handle specific error types
  if (hasZodFastifySchemaValidationErrors(error)) {
    return reply.code(400).send({
      error: 'Validation Error',
      message: 'Request validation failed',
      statusCode: 400,
      issues: error.validation.map(formatValidationIssue)
    });
  }

  if (error instanceof APIError) {
    return reply.status(error.statusCode).send({
      error: error.error,
      message: error.message,
      statusCode: error.statusCode,
      ...(error.context && { context: error.context })
    });
  }

  // Default error response
  return reply.status(500).send({
    error: 'Internal Server Error',
    message: 'An unexpected error occurred',
    statusCode: 500
  });
};
```

### 3. Error Logging

#### Structured Logging
```typescript
// Log levels and structure
const logError = (
  logger: FastifyBaseLogger,
  error: Error,
  context: LogContext
) => {
  logger.error({
    error: {
      name: error.name,
      message: error.message,
      stack: error.stack
    },
    request: {
      id: context.requestId,
      method: context.method,
      url: context.url,
      userAgent: context.userAgent
    },
    user: {
      id: context.userId,
      role: context.userRole
    },
    timestamp: new Date().toISOString()
  });
};
```

---

## Deployment Best Practices

### 1. Environment Configuration

#### Production Settings
```typescript
// Environment-specific configuration
const getConfig = () => {
  const env = process.env.NODE_ENV || 'development';
  
  const baseConfig = {
    host: '0.0.0.0',
    port: parseInt(process.env.PORT || '3000'),
    logger: env === 'production' ? true : {
      level: 'debug',
      prettyPrint: true
    }
  };
  
  if (env === 'production') {
    return {
      ...baseConfig,
      trustProxy: true,
      disableRequestLogging: false,
      keepAliveTimeout: 30000,
      requestTimeout: 30000
    };
  }
  
  return baseConfig;
};
```

### 2. Health Checks

#### Monitoring Endpoints
```typescript
// Health check implementation
fastify.get('/health', {
  schema: {
    response: {
      200: z.object({
        status: z.string(),
        timestamp: z.string(),
        uptime: z.number(),
        version: z.string(),
        dependencies: z.object({
          database: z.string(),
          redis: z.string().optional()
        })
      })
    }
  }
}, async (request, reply) => {
  const healthCheck = {
    status: 'healthy',
    timestamp: new Date().toISOString(),
    uptime: process.uptime(),
    version: process.env.npm_package_version || '1.0.0',
    dependencies: {
      database: await checkDatabaseHealth(),
      redis: await checkRedisHealth()
    }
  };
  
  return reply.send(healthCheck);
});

// Readiness check
fastify.get('/ready', async (request, reply) => {
  try {
    await fastify.prisma.$queryRaw`SELECT 1`;
    return reply.send({ status: 'ready' });
  } catch (error) {
    return reply.status(503).send({ status: 'not ready', error: error.message });
  }
});
```

### 3. Security Headers

#### Production Security
```typescript
// Security headers middleware
fastify.register(async (fastify) => {
  fastify.addHook('onSend', async (request, reply) => {
    reply.headers({
      'X-Content-Type-Options': 'nosniff',
      'X-Frame-Options': 'DENY',
      'X-XSS-Protection': '1; mode=block',
      'Strict-Transport-Security': 'max-age=31536000; includeSubDomains',
      'Content-Security-Policy': "default-src 'self'",
      'Referrer-Policy': 'strict-origin-when-cross-origin'
    });
  });
});
```

### 4. Performance Monitoring

#### Metrics Collection
```typescript
// Performance metrics
const performanceMetrics = {
  requestDuration: new Map<string, number>(),
  errorCount: new Map<string, number>(),
  activeConnections: 0
};

fastify.addHook('onRequest', async (request) => {
  request.startTime = Date.now();
  performanceMetrics.activeConnections++;
});

fastify.addHook('onResponse', async (request, reply) => {
  const duration = Date.now() - request.startTime;
  const route = `${request.method} ${request.routerPath}`;
  
  performanceMetrics.requestDuration.set(route, duration);
  performanceMetrics.activeConnections--;
  
  // Log slow requests
  if (duration > 1000) {
    request.log.warn({
      route,
      duration,
      message: 'Slow request detected'
    });
  }
});
```
<!-- SECTION_END: Development Best Practices and Patterns -->

---

<!-- DOCUMENT_METADATA_END
This tech stack and best practices documentation has been optimized for LLM parsing and embedding generation with the following enhancements:
- Added comprehensive document metadata and keywords for better searchability and categorization
- Enhanced section markers (SECTION_START/SECTION_END) for improved document chunking and semantic segmentation
- Structured information with detailed explanations, business context, and technical implementation details for each technology
- Added explicit purpose, implementation strategies, benefits, and impact statements for better understanding
- Included comprehensive technology descriptions with use cases, integration details, and architectural context
- Enhanced best practice explanations with implementation details, benefits, and real-world application guidance
- Structured development patterns with clear responsibilities, relationships, and practical examples
- Added detailed context for when and why specific patterns, technologies, and practices should be used
- Improved code example explanations with comprehensive comments, business purpose, and architectural significance
- Optimized for semantic search and knowledge extraction by AI systems and documentation tools
- Enhanced readability and parsing for automated documentation systems and knowledge management
- Added comprehensive monitoring and observability practices with production-ready implementation guidance
- Structured security, performance, and deployment information with practical implementation details
- Improved development workflow documentation with clear processes and tooling integration
- Enhanced for embedding generation with rich context, detailed explanations, and structured information hierarchy
- Organized content with consistent formatting patterns and semantic structure for optimal LLM understanding
- Added comprehensive cross-references and contextual relationships between different sections and concepts
- Structured for maximum value extraction by AI systems while maintaining human readability and usability
-->
