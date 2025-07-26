# Frontend Architecture Documentation

<!-- DOCUMENT_METADATA
Document Type: Technical Architecture Documentation
Project: Markit Frontend Application
Framework: Next.js 15 with React 19
Architecture Pattern: Domain-Driven Design
Last Updated: 2024
Purpose: Comprehensive guide to frontend architecture, patterns, and implementation details
-->

<!-- KEYWORDS: NextJS, React, TypeScript, Domain-Driven-Design, Component-Architecture, State-Management, Frontend-Architecture, Markit -->

## Table of Contents
1. [Overview](#overview) - Application overview and core principles
2. [Technology Stack](#technology-stack) - Complete technology stack and versions
3. [Project Structure](#project-structure) - File organization and folder structure
4. [Architectural Patterns](#architectural-patterns) - Design patterns and architecture approaches
5. [Domain-Driven Design](#domain-driven-design) - Business domain organization
6. [Component Architecture](#component-architecture) - UI component design and patterns
7. [State Management](#state-management) - Client and server state management
8. [Data Layer](#data-layer) - API integration and data fetching
9. [Routing & Navigation](#routing--navigation) - Next.js App Router implementation
10. [Form Handling & Validation](#form-handling--validation) - Form management and validation
11. [UI Design System](#ui-design-system) - Design tokens and component library
12. [Configuration & Environment](#configuration--environment) - Environment setup and configuration
13. [Performance Optimizations](#performance-optimizations) - Performance patterns and optimizations
14. [Development Patterns](#development-patterns) - Common development patterns and practices
15. [Best Practices](#best-practices) - Code quality and development standards

## Overview

<!-- SECTION_START: Application Overview -->
**Context**: The Markit frontend application is a comprehensive marketing strategy platform that helps users create marketing briefs and generate AI-driven marketing strategies.

**Technical Foundation**: The application is built as a modern, scalable React application using Next.js 15 with the App Router architecture. The frontend implements domain-driven design principles with feature-based organization patterns.

**Primary Purpose**: This frontend serves as a marketing strategy platform that provides:
- Marketing brief creation workflows
- AI-driven marketing strategy recommendations  
- Expert strategy review and editing capabilities
- Analytics and performance tracking dashboards

### Key Architecture Principles

**Principle 1: Domain-Driven Design (DDD)**
- Business logic is organized by functional domains (brief, strategy, user, location)
- Each domain contains its own API layer, types, constants, and state management
- Domain boundaries align with business capabilities and user workflows

**Principle 2: Feature-Based Structure** 
- UI modules are organized by user-facing features rather than technical concerns
- Each feature module contains components, validation, utilities, and constants
- Features are designed for modularity and independent development

**Principle 3: Component Composition**
- UI components are built using composition patterns over inheritance
- Reusable components are designed with flexible APIs and variant support
- Component libraries follow atomic design principles

**Principle 4: Type Safety**
- Full TypeScript coverage with strict typing enabled
- Runtime validation using Zod schemas for external data
- Type-safe API clients and state management

**Principle 5: Server Components**
- Leverages Next.js 15 App Router features including Server Components
- Optimized data fetching using React Server Components
- Reduced JavaScript bundle size through server-side rendering

**Principle 6: Performance First**
- Optimized rendering through React 19 concurrent features
- Efficient data fetching with React Query caching strategies
- Code splitting and lazy loading for optimal bundle sizes
<!-- SECTION_END: Application Overview -->

## Technology Stack

<!-- SECTION_START: Technology Stack -->
**Overview**: The Markit frontend technology stack is built on modern React ecosystem tools, prioritizing type safety, developer experience, and performance.

### Core Framework Technologies

**Next.js 15.2.1 - Primary React Framework**
- **Purpose**: Full-stack React framework providing the application foundation
- **Key Features**: App Router architecture, Server Components, automatic code splitting
- **Use Case**: Handles routing, server-side rendering, and application structure
- **Benefits**: Optimized performance, SEO-friendly, built-in optimizations

**React 19 - UI Library**
- **Purpose**: Core UI library for building component-based user interfaces
- **Key Features**: Concurrent rendering, Suspense, Server Components support
- **Use Case**: Component rendering, state management, user interaction handling
- **Benefits**: Latest React features, improved performance, better developer experience

**TypeScript 5 - Type System**
- **Purpose**: Static type checking and enhanced developer experience
- **Key Features**: Strict typing, advanced type inference, modern ECMAScript support
- **Use Case**: Type safety across the entire application codebase
- **Benefits**: Reduced runtime errors, better IDE support, improved maintainability

### State Management & Data Fetching Technologies

**Zustand 5.0.3 - Client State Management**
- **Purpose**: Lightweight state management for client-side application state
- **Key Features**: Simple API, TypeScript support, persistence, devtools integration
- **Use Case**: User session state, UI preferences, global application state
- **Benefits**: Minimal boilerplate, excellent performance, small bundle size

**TanStack Query 5.67.2 - Server State Management**
- **Purpose**: Data fetching, caching, and synchronization with server state
- **Key Features**: Automatic caching, background updates, error handling, optimistic updates
- **Use Case**: API data management, server state synchronization, loading states
- **Benefits**: Reduced boilerplate, automatic caching, improved user experience

**ky-universal 0.12.0 - HTTP Client**
- **Purpose**: Modern HTTP client for API communication
- **Key Features**: Promise-based, request/response interceptors, TypeScript support
- **Use Case**: API requests, authentication headers, error handling
- **Benefits**: Modern API, better error handling, TypeScript integration

### UI & Styling Technologies

**Tailwind CSS 4 - Utility-First CSS Framework**
- **Purpose**: Rapid UI development with utility-first CSS approach
- **Key Features**: Utility classes, responsive design, dark mode, design tokens
- **Use Case**: Component styling, responsive layouts, design system implementation
- **Benefits**: Consistent styling, rapid development, small production bundles

**Radix UI - Accessible UI Primitives**
- **Purpose**: Unstyled, accessible UI components as building blocks
- **Key Features**: Full accessibility support, keyboard navigation, ARIA compliance
- **Use Case**: Complex UI components (modals, dropdowns, forms)
- **Benefits**: Accessibility by default, customizable styling, robust behavior

**shadcn/ui - Pre-built Component Library**
- **Purpose**: Pre-styled components built on Radix UI primitives
- **Key Features**: Copy-paste components, Tailwind CSS integration, TypeScript support
- **Use Case**: Rapid UI development with consistent design patterns
- **Benefits**: Time savings, consistent design, maintained component patterns

**Lucide React - Icon Library**
- **Purpose**: Comprehensive icon set for user interface elements
- **Key Features**: SVG-based icons, tree-shakeable, consistent design
- **Use Case**: UI icons, interactive elements, visual indicators
- **Benefits**: Lightweight, consistent style, good performance

**next-themes - Theme Management**
- **Purpose**: Dark/light mode theme switching functionality
- **Key Features**: Automatic theme detection, smooth transitions, SSR support
- **Use Case**: User theme preferences, dark/light mode toggle
- **Benefits**: Improved user experience, accessibility, modern UI expectations

### Form Management Technologies

**React Hook Form 7.54.2 - Form State Management**
- **Purpose**: Performant form handling with minimal re-renders
- **Key Features**: Uncontrolled components, validation integration, TypeScript support
- **Use Case**: Complex forms, user input handling, form validation
- **Benefits**: Better performance, less boilerplate, flexible validation

**Zod 3.24.2 - Runtime Type Validation**
- **Purpose**: Schema validation and type inference for runtime data
- **Key Features**: TypeScript integration, custom validation, error handling
- **Use Case**: Form validation, API response validation, data transformation
- **Benefits**: Type safety, runtime validation, excellent error messages

**@hookform/resolvers - Validation Integration**
- **Purpose**: Bridge between React Hook Form and validation libraries
- **Key Features**: Seamless integration, multiple resolver support
- **Use Case**: Connecting Zod schemas with React Hook Form
- **Benefits**: Simplified integration, consistent validation patterns

### Developer Experience Technologies

**ESLint 9 - Code Quality**
- **Purpose**: Static analysis tool for identifying and fixing code issues
- **Key Features**: Customizable rules, TypeScript support, auto-fixing
- **Use Case**: Code quality enforcement, consistent coding standards
- **Benefits**: Reduced bugs, consistent code style, improved maintainability

**Prettier - Code Formatting**
- **Purpose**: Automatic code formatting for consistent style
- **Key Features**: Language support, configurable rules, editor integration
- **Use Case**: Code formatting, style consistency across team
- **Benefits**: Consistent code style, reduced style discussions, automated formatting

**PostHog - Analytics and Feature Flags**
- **Purpose**: Product analytics and feature flag management
- **Key Features**: Event tracking, user analytics, A/B testing, feature flags
- **Use Case**: User behavior tracking, feature rollouts, product insights
- **Benefits**: Data-driven decisions, controlled feature releases, user insights

### Additional Supporting Libraries

**react-markdown - Markdown Rendering**
- **Purpose**: Render markdown content as React components
- **Key Features**: Customizable renderers, plugin support, security features
- **Use Case**: Dynamic content rendering, documentation display
- **Benefits**: Flexible content rendering, security, React integration

**file-saver - File Download Functionality**
- **Purpose**: Client-side file saving capabilities
- **Key Features**: Cross-browser support, various file formats
- **Use Case**: Exporting strategies, downloading reports
- **Benefits**: Simple API, reliable downloads, browser compatibility

**js-cookie - Cookie Management**
- **Purpose**: Simple cookie manipulation library
- **Key Features**: Lightweight API, encoding support, security options
- **Use Case**: Authentication tokens, user preferences storage
- **Benefits**: Simple API, reliable cookie handling, security features

**sonner - Toast Notifications**
- **Purpose**: Beautiful toast notification system
- **Key Features**: Customizable styling, positioning, animations
- **Use Case**: User feedback, success/error messages, notifications
- **Benefits**: Great user experience, customizable, accessible
<!-- SECTION_END: Technology Stack -->

## Project Structure

<!-- SECTION_START: Project Structure -->
**Overview**: The Markit frontend follows a domain-driven, feature-based organization pattern that separates concerns by business domains and user-facing features.

### Directory Structure Explanation

**Root Client Directory Structure:**
```
client/
├── app/                          # Next.js App Router pages and layouts
├── components/                   # Reusable UI component library  
├── config/                      # Application configuration and setup
├── constants/                   # Application-wide constants and definitions
├── domains/                     # Domain-driven business logic organization
├── lib/                         # Shared utility libraries and helpers
├── modules/                     # Feature-based UI modules and workflows
├── types/                       # Global TypeScript type definitions
└── middleware.ts                # Next.js middleware for request interception
```

### App Directory - Next.js App Router Pages
**Purpose**: Contains all Next.js App Router pages, layouts, and route-specific components
**Location**: `app/`

**Key Directories:**
- **`(with-header)/`** - Route group that includes the main navigation header
  - Contains: dashboard, strategy, analytics pages
  - Purpose: Main application pages that require header navigation
  
- **`[...not-found]/`** - Dynamic catch-all route for 404 error handling
  - Contains: Custom 404 page component
  - Purpose: Provides user-friendly error page for invalid routes
  
- **`brief/[step]/`** - Dynamic route for multi-step brief creation process
  - Contains: Step-based form layouts and page components  
  - Purpose: Handles the marketing brief creation workflow
  
- **`expert/`** - Expert user interface and expert-specific pages
  - Contains: Expert dashboard, brief review, strategy editing pages
  - Purpose: Provides expert user functionality and workflows
  
- **`globals.css`** - Global CSS styles and Tailwind CSS imports
- **`layout.tsx`** - Root layout component with providers and global setup
- **`providers.tsx`** - Global context providers (React Query, theme, etc.)

### Components Directory - Reusable UI Components
**Purpose**: Contains the application's component library and design system
**Location**: `components/`

**Subdirectories:**
- **`shared/`** - Business logic components used across multiple features
  - Examples: header navigation, location selectors, mobile alerts
  - Purpose: Reusable components with business logic
  
- **`ui/`** - Design system components built on Radix UI and Tailwind
  - Examples: buttons, forms, modals, cards, inputs
  - Purpose: Foundational UI building blocks with consistent styling

### Config Directory - Application Configuration  
**Purpose**: Centralized configuration management and environment setup
**Location**: `config/`

**Files:**
- **`api.ts`** - HTTP client configuration with authentication and error handling
- **`env.ts`** - Environment variable validation and type-safe access

### Constants Directory - Application Constants
**Purpose**: Centralized constant definitions used throughout the application
**Location**: `constants/`

**Files:**
- **`api-routes.ts`** - Backend API endpoint URL definitions
- **`general.ts`** - General application constants and enumerations  
- **`routes.ts`** - Frontend route path definitions and navigation helpers

### Domains Directory - Business Logic Organization
**Purpose**: Domain-driven design implementation with business logic separation
**Location**: `domains/`

**Domain Structure:** Each domain contains:
- API layer functions for HTTP requests
- TypeScript type definitions
- React Query hooks for data fetching
- Zustand stores for state management
- Domain-specific constants

**Business Domains:**
- **`brief/`** - Marketing brief creation and management
  - Subdomains: business-information, competitors, marketing-goals, etc.
  - Purpose: Handles all brief-related business logic
  
- **`location/`** - Geographic location services and data
  - Purpose: Country/region selection and location-based functionality
  
- **`strategy/`** - Marketing strategy management and editing
  - Purpose: Strategy creation, editing, and export functionality
  
- **`user/`** - User authentication and profile management
  - Purpose: User session, authentication, and profile data

### Lib Directory - Utility Libraries
**Purpose**: Shared utility functions and helper libraries
**Location**: `lib/`

**Files:**
- **`utils.ts`** - Common utility functions, class name helpers, data transformations

### Modules Directory - Feature-Based UI Organization
**Purpose**: User-facing feature implementations with complete UI workflows
**Location**: `modules/`

**Feature Modules:**
- **`brief-steps/`** - Multi-step brief creation form workflow
  - Subdirectories: business-information, competitors, marketing-goals, etc.
  - Structure: components, validation, utilities, constants per step
  
- **`dashboard/`** - User dashboard with overview and quick actions
  - Components: dashboard cards, loading states, navigation
  
- **`strategy/`** - Strategy viewing and interaction components
  - Components: strategy display, export options, sharing features
  
- **Authentication Modules** - Sign-in, sign-up, password management
  - Examples: sign-in, sign-up, forgot-password, verify-email

**Module Structure Pattern:** Each module contains:
- `index.tsx` - Main module component
- `components/` - Module-specific UI components
- `validation/` - Form validation schemas
- `utils/` - Module-specific utility functions
- `constants/` - Module-specific constants

### Types Directory - Global Type Definitions
**Purpose**: Application-wide TypeScript type definitions and interfaces
**Location**: `types/`

**Files:**
- **`general.ts`** - Common types used across multiple domains and features

### Middleware - Request Interception
**Purpose**: Next.js middleware for authentication, redirects, and request processing
**Location**: `middleware.ts`

**Functionality:**
- Authentication checks for protected routes
- Automatic redirects for unauthorized users
- Request/response manipulation for security and routing
<!-- SECTION_END: Project Structure -->

## Architectural Patterns

<!-- SECTION_START: Architectural Patterns -->
**Overview**: The Markit frontend implements three core architectural patterns that work together to create a maintainable, scalable, and organized codebase.

### Pattern 1: Domain-Driven Design (DDD)
**Purpose**: Organizes business logic around business domains rather than technical concerns
**Implementation**: Business logic is separated into distinct domains that mirror real-world business capabilities

**Domain Components**: Each domain contains the following standardized components:
- **API Layer** - HTTP client functions for domain-specific server communication
- **Types** - TypeScript type definitions specific to the domain's data structures  
- **Constants** - Domain-specific constants, enumerations, and configuration values
- **Queries** - React Query hooks for data fetching and server state management
- **Mutations** - React Query hooks for data modifications and server updates
- **Stores** - Zustand stores for domain-specific client state management

**Benefits of DDD Approach**:
- Clear separation of business concerns
- Improved maintainability through domain isolation
- Better team collaboration with domain ownership
- Reduced coupling between different business areas
- Easier testing and debugging of domain-specific logic

### Pattern 2: Feature-Based Module Organization
**Purpose**: Organizes UI components and logic around user-facing features rather than technical file types
**Implementation**: UI modules are structured around complete user workflows and feature sets

**Module Components**: Each feature module contains:
- **Index Component** - Main entry point component that orchestrates the feature
- **Sub-components** - Feature-specific UI components and layouts
- **Validation** - Form validation schemas using Zod for type-safe validation
- **Utils** - Feature-specific utility functions and helper methods
- **Constants** - Feature-specific constants, default values, and configuration

**Feature Module Examples**:
- **Brief Steps Module** - Handles the multi-step marketing brief creation workflow
- **Dashboard Module** - Manages user dashboard interface and data display
- **Strategy Module** - Handles strategy viewing, editing, and export functionality
- **Authentication Modules** - Manages sign-in, sign-up, and password workflows

**Benefits of Feature-Based Organization**:
- Improved developer experience with feature-focused development
- Better code locality with related functionality grouped together
- Easier feature maintenance and updates
- Simplified testing with isolated feature components
- Enhanced team productivity with clear feature boundaries

### Pattern 3: Layered Architecture
**Purpose**: Separates application concerns into distinct layers with clear responsibilities and dependencies
**Implementation**: Four-layer architecture with unidirectional dependencies

**Architecture Layers**:
```
┌─────────────────────────────────────┐
│           Presentation Layer        │  (Pages, Modules, Components)
├─────────────────────────────────────┤
│           Business Logic Layer      │  (Domains, Stores, Mutations)
├─────────────────────────────────────┤
│           Data Access Layer         │  (API, React Query, HTTP Client)
├─────────────────────────────────────┤
│           Infrastructure Layer      │  (Config, Constants, Utils)
└─────────────────────────────────────┘
```

**Layer Descriptions**:

**Presentation Layer** - User Interface and Interaction
- **Components**: React components, pages, and UI modules
- **Responsibilities**: User interaction handling, data presentation, routing
- **Technologies**: Next.js App Router, React components, Tailwind CSS
- **Dependencies**: Can access Business Logic Layer and below

**Business Logic Layer** - Application Logic and State Management
- **Components**: Domain logic, state stores, business rules
- **Responsibilities**: Business process implementation, application state management
- **Technologies**: Zustand stores, React Query mutations, domain services
- **Dependencies**: Can access Data Access Layer and below

**Data Access Layer** - External Data Communication
- **Components**: API clients, data fetching, server state management
- **Responsibilities**: HTTP communication, data transformation, caching
- **Technologies**: React Query, ky-universal HTTP client, API integrations
- **Dependencies**: Can access Infrastructure Layer only

**Infrastructure Layer** - Configuration and Utilities
- **Components**: Configuration, constants, utility functions
- **Responsibilities**: Environment setup, shared utilities, cross-cutting concerns
- **Technologies**: Environment validation, utility libraries, constants
- **Dependencies**: No dependencies on other application layers

**Benefits of Layered Architecture**:
- Clear separation of concerns with defined responsibilities
- Predictable data flow and dependency management
- Improved testability through layer isolation
- Better maintainability with organized code structure
- Enhanced scalability through modular design
<!-- SECTION_END: Architectural Patterns -->

## Domain-Driven Design

<!-- SECTION_START: Domain-Driven Design Implementation -->
**Overview**: The Markit frontend implements Domain-Driven Design (DDD) to organize business logic around real-world business domains, creating clear boundaries and ownership.

### Business Domain Organization

#### Brief Domain - Marketing Brief Management
**Location**: `domains/brief/`
**Purpose**: Handles the complete marketing brief creation and management process
**Business Context**: Manages the workflow for creating comprehensive marketing briefs through structured data collection

**Brief Domain Subdomains**:
- **business-information/** - Company details, industry, and basic setup information
  - Data: Company name, website, industry, business model, company size
  - API: CRUD operations for business information
  - Validation: Company data validation and URL verification
  
- **competitors/** - Competitor analysis and competitive branding research
  - Data: Competitor names, websites, branding analysis, market positioning
  - API: Competitor data management and analysis endpoints
  - Validation: Competitor information and branding data validation
  
- **marketing-goals/** - Marketing objectives and strategic goal definition
  - Data: Marketing objectives, target metrics, timeline, strategic goals
  - API: Goal setting and objective management endpoints
  - Validation: Goal feasibility and metric validation
  
- **marketing-resources/** - Budget allocation and marketing channel selection
  - Data: Budget constraints, channel preferences, resource allocation
  - API: Resource management and budget tracking endpoints
  - Validation: Budget and resource constraint validation
  
- **strategy-adjustments/** - Success metrics and strategy adjustment preferences
  - Data: Success metrics, KPIs, adjustment preferences, measurement criteria
  - API: Metrics management and adjustment tracking endpoints
  - Validation: Metrics feasibility and measurement validation
  
- **target-audience/** - Customer demographics and market definition
  - Data: Customer personas, demographics, market segments, audience characteristics
  - API: Audience management and segmentation endpoints
  - Validation: Audience data and demographic validation

#### User Domain - Authentication and Profile Management
**Location**: `domains/user/`
**Purpose**: Manages user authentication, session management, and profile data
**Business Context**: Handles user identity, access control, and personalization

**User Domain Components**:
- **Authentication** - User login, registration, and password management workflows
  - Data: User credentials, session tokens, authentication state
  - API: Authentication endpoints, token management, password operations
  - Security: JWT token handling, secure password storage, session management
  
- **Profile** - User personal data, preferences, and account settings
  - Data: User profile information, preferences, account settings
  - API: Profile management endpoints, preference updates
  - Validation: Profile data validation and preference constraints
  
- **State** - User session management and application state persistence
  - Data: Session state, user preferences, application settings
  - Storage: Local storage persistence, session management
  - Management: State synchronization and cross-tab communication

#### Strategy Domain - Marketing Strategy Management
**Location**: `domains/strategy/`
**Purpose**: Handles marketing strategy creation, editing, and management workflows
**Business Context**: Manages generated marketing strategies and expert editing capabilities

**Strategy Domain Components**:
- **Strategy** - Core strategy creation, editing, and version management
  - Data: Strategy content, metadata, version history, status tracking
  - API: Strategy CRUD operations, version management endpoints
  - Management: Strategy lifecycle, approval workflows, publishing
  
- **Blocks** - Strategy content blocks and modular strategy components
  - Data: Content blocks, block templates, block relationships
  - API: Block management endpoints, template operations
  - Structure: Modular content system, block composition, reusability
  
- **Export** - Strategy download, sharing, and external integration capabilities
  - Data: Export formats, sharing permissions, external integrations
  - API: Export generation endpoints, sharing management
  - Formats: PDF generation, document formats, sharing options

#### Location Domain - Geographic Services
**Location**: `domains/location/`
**Purpose**: Provides location-based services and geographic data management
**Business Context**: Handles geographic targeting and location-based business logic

**Location Domain Components**:
- **Geolocation** - Country, region, and geographic data management
  - Data: Country codes, region information, geographic hierarchies
  - API: Location data endpoints, geographic search capabilities
  - Services: Location lookup, geographic validation, region mapping
  
- **Validation** - Location-based validation and geographic constraint checking
  - Data: Geographic constraints, location rules, validation criteria
  - API: Validation endpoints, constraint checking services
  - Logic: Geographic business rules, location-specific validation

### Domain Structure Pattern
**Consistency**: Each domain follows a standardized file structure for maintainability and predictability

**Standard Domain Structure**:
```typescript
// domains/[domain]/
├── api.ts                 # HTTP client functions for domain operations
├── constants.ts           # Domain-specific constants and enumerations
├── types.ts              # TypeScript type definitions for domain data
├── queries.ts            # React Query hooks for data fetching
├── mutations.ts          # React Query hooks for data mutations
├── index.ts              # Public API exports and domain interface
└── [subdomain]/          # Subdomain organization for complex domains
    ├── api.ts            # Subdomain-specific API functions
    ├── constants.ts      # Subdomain constants and configurations
    ├── types.ts          # Subdomain type definitions
    ├── queries.ts        # Subdomain React Query hooks
    └── mutations.ts      # Subdomain mutation hooks
```

**File Responsibilities**:
- **api.ts** - Contains HTTP client functions using ky-universal for server communication
- **constants.ts** - Defines domain-specific constants, enums, and default values
- **types.ts** - TypeScript interfaces and types for domain data structures
- **queries.ts** - React Query hooks for data fetching with caching and error handling
- **mutations.ts** - React Query hooks for data modifications with optimistic updates
- **index.ts** - Public exports and domain boundary definition

**Benefits of Standardized Structure**:
- Predictable file organization across all domains
- Consistent developer experience when working with different domains
- Simplified onboarding for new team members
- Clear separation of concerns within each domain
- Standardized patterns for testing and maintenance
<!-- SECTION_END: Domain-Driven Design Implementation -->

## Component Architecture

### Design System Components (`components/ui/`)
Built on Radix UI primitives with shadcn/ui styling:

```typescript
// Example: Button component
export interface ButtonProps 
  extends React.ButtonHTMLAttributes<HTMLButtonElement>,
    VariantProps<typeof buttonVariants> {
  asChild?: boolean;
}

const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
  ({ className, variant, size, asChild = false, ...props }, ref) => {
    const Comp = asChild ? Slot : "button";
    return (
      <Comp
        className={cn(buttonVariants({ variant, size, className }))}
        ref={ref}
        {...props}
      />
    );
  }
);
```

### Shared Components (`components/shared/`)
Business logic components used across features:
- **header.tsx**: Navigation header
- **expert-header.tsx**: Expert user header
- **location-select.tsx**: Location selection
- **mobile-alert.tsx**: Mobile responsiveness alert

### Component Patterns

#### 1. Compound Components
```typescript
// Card compound component pattern
<Card>
  <CardHeader>
    <CardTitle>Title</CardTitle>
    <CardDescription>Description</CardDescription>
  </CardHeader>
  <CardContent>Content</CardContent>
  <CardFooter>
    <CardAction>Action</CardAction>
  </CardFooter>
</Card>
```

#### 2. Polymorphic Components
```typescript
// Using asChild pattern for composition
<Button asChild>
  <Link href="/dashboard">Go to Dashboard</Link>
</Button>
```

#### 3. Controlled vs Uncontrolled
Components support both patterns based on use case:
```typescript
// Controlled
<Select value={value} onValueChange={setValue}>
  
// Uncontrolled  
<Select defaultValue="default">
```

## State Management

### Zustand Stores
Lightweight state management for client-side state:

```typescript
// User store example
export const useUserStore = create<UserStore>()(
  persist(
    (set, get) => ({
      user: null,
      setUser: (user: User | null) => set({ user }),
    }),
    {
      name: "user-storage",
      storage: createJSONStorage(() => localStorage),
    },
  ),
);
```

### State Categories

#### 1. Server State (React Query)
- API responses
- Cached data
- Loading states
- Error states

#### 2. Client State (Zustand)
- User session
- UI preferences
- Form state (complex forms)
- Modal states

#### 3. URL State (Next.js Router)
- Route parameters
- Search params
- Navigation state

#### 4. Local Component State (useState)
- Temporary UI state
- Form inputs (simple forms)
- Toggle states

## Data Layer

### React Query Integration

#### Query Configuration
```typescript
const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      refetchOnWindowFocus: false,
      retry: false,
    },
  },
});
```

#### Query Patterns
```typescript
// Standard query hook
export const useGetBusinessInformationQuery = () =>
  useQuery({
    queryKey: businessInformationQueryKeys.details(),
    queryFn: getBusinessInformation,
  });

// Mutation hook
export const useCreateBusinessInformationMutation = () =>
  useMutation({
    mutationFn: createBusinessInformation,
    onSuccess: () => {
      queryClient.invalidateQueries({
        queryKey: businessInformationQueryKeys.all,
      });
    },
  });
```

### API Client Configuration

```typescript
// ky-universal HTTP client
const api = ky.create({
  prefixUrl: env.NEXT_PUBLIC_API_URL,
  timeout: false,
  hooks: {
    beforeRequest: [
      (request) => {
        const token = Cookies.get("token");
        if (token) {
          request.headers.set("Authorization", `Bearer ${token}`);
        }
      },
    ],
    beforeError: [
      async (error) => {
        if (error.response.status === 401) {
          // Handle unauthorized access
          useUserStore.getState().setUser(null);
          Cookies.remove("token");
          window.location.href = routes.signIn;
        }
        return error;
      },
    ],
  },
});
```

## Routing & Navigation

### App Router Structure
Using Next.js 15 App Router with file-based routing:

```
app/
├── layout.tsx                    # Root layout
├── page.tsx                      # Home page (redirects)
├── (with-header)/               # Route group with header
│   ├── layout.tsx               # Header layout
│   ├── dashboard/page.tsx       # Dashboard page
│   ├── strategy/page.tsx        # Strategy page
│   └── analytics/page.tsx       # Analytics page
├── brief/[step]/                # Dynamic brief steps
│   ├── layout.tsx               # Brief layout
│   └── page.tsx                 # Step content
├── expert/                      # Expert interface
│   ├── layout.tsx               # Expert layout
│   ├── dashboard/page.tsx       # Expert dashboard
│   ├── briefs/[id]/page.tsx     # Brief details
│   └── strategies/[id]/page.tsx # Strategy editing
└── [...not-found]/page.tsx      # 404 page
```

### Route Constants
Centralized route management:

```typescript
export const routes = {
  signIn: "/sign-in",
  signUp: "/sign-up",
  dashboard: "/dashboard",
  strategy: "/strategy",
  analytics: "/analytics",
  briefStep: (step: BriefFormSteps) => `/brief/${step}`,
  expertBrief: (id: string) => `/expert/briefs/${id}`,
  expertStrategy: (id: string) => `/expert/strategies/${id}`,
};
```

### Middleware
Request interception for authentication:

```typescript
export function middleware(request: NextRequest) {
  if (request.nextUrl.pathname === routes.home) {
    return NextResponse.redirect(new URL(routes.signIn, request.url));
  }
}
```

## Form Handling & Validation

### React Hook Form + Zod Integration

#### Validation Schema Pattern
```typescript
// Zod schema with custom validation
export const businessInformationFormSchema = z
  .object({
    name: z.string().min(1, { message: "Name is required" }),
    website: z.string().optional(),
    industry: z.string().min(1, { message: "Industry is required" }),
    // ... other fields
  })
  .superRefine((data, ctx) => {
    // Custom validation logic
    if (data.website && !z.string().url().safeParse(data.website).success) {
      ctx.addIssue({
        code: z.ZodIssueCode.custom,
        message: "Please enter a valid URL",
        path: ["website"],
      });
    }
  });
```

#### Form Implementation
```typescript
const form = useForm<BusinessInformationFormValues>({
  resolver: zodResolver(businessInformationFormSchema),
  defaultValues: {
    name: "",
    website: "",
    // ... other defaults
  },
});

const onSubmit = (values: BusinessInformationFormValues) => {
  // Form submission logic
};
```

### Form Component Patterns

#### Field Component Pattern
```typescript
<FormField
  control={form.control}
  name="name"
  render={({ field }) => (
    <FormItem>
      <FormLabel>Company Name</FormLabel>
      <FormControl>
        <Input placeholder="Enter company name" {...field} />
      </FormControl>
      <FormMessage />
    </FormItem>
  )}
/>
```

## UI Design System

### Tailwind Configuration
Modern Tailwind CSS 4 with design tokens:

```css
/* Design tokens in CSS variables */
:root {
  --background: 0 0% 100%;
  --foreground: 240 10% 3.9%;
  --primary: 142 70% 45%;
  --primary-foreground: 356 29% 98%;
  /* ... other tokens */
}
```

### Component Variants
Using `class-variance-authority` for component variants:

```typescript
const buttonVariants = cva(
  "inline-flex items-center justify-center rounded-md text-sm font-medium",
  {
    variants: {
      variant: {
        default: "bg-primary text-primary-foreground hover:bg-primary/90",
        destructive: "bg-destructive text-destructive-foreground",
        outline: "border border-input bg-background hover:bg-accent",
      },
      size: {
        default: "h-10 px-4 py-2",
        sm: "h-9 rounded-md px-3",
        lg: "h-11 rounded-md px-8",
      },
    },
    defaultVariants: {
      variant: "default",
      size: "default",
    },
  }
);
```

### Typography System
Consistent typography components:

```typescript
export function TypographyH1({ 
  children, 
  className 
}: TypographyProps) {
  return (
    <h1 className={cn(
      "scroll-m-20 text-4xl font-extrabold tracking-tight lg:text-5xl",
      className
    )}>
      {children}
    </h1>
  );
}
```

## Configuration & Environment

### Type-Safe Environment Variables
Using `@t3-oss/env-nextjs` for runtime validation:

```typescript
export const env = createEnv({
  client: {
    NEXT_PUBLIC_API_URL: z.string().url(),
    NEXT_PUBLIC_CSC_API_KEY: z.string(),
    NEXT_PUBLIC_POSTHOG_KEY: z.string(),
    NEXT_PUBLIC_POSTHOG_HOST: z.string(),
  },
  server: {},
  runtimeEnv: {
    NEXT_PUBLIC_API_URL: process.env.NEXT_PUBLIC_API_URL,
    NEXT_PUBLIC_CSC_API_KEY: process.env.NEXT_PUBLIC_CSC_API_KEY,
    NEXT_PUBLIC_POSTHOG_KEY: process.env.NEXT_PUBLIC_POSTHOG_KEY,
    NEXT_PUBLIC_POSTHOG_HOST: process.env.NEXT_PUBLIC_POSTHOG_HOST,
  },
});
```

### TypeScript Configuration
Strict TypeScript with path mapping:

```json
{
  "compilerOptions": {
    "strict": true,
    "noEmit": true,
    "moduleResolution": "bundler",
    "jsx": "preserve",
    "paths": {
      "@/*": ["./*"]
    }
  }
}
```

## Performance Optimizations

### React Query Optimizations
- Selective invalidation with query keys
- Background refetching disabled by default
- Retry logic disabled for predictable behavior

### Next.js Optimizations
- App Router for automatic code splitting
- Server Components where possible
- Image optimization with Next.js Image
- Font optimization with next/font

### Bundle Optimization
- Tree shaking with ES modules
- Dynamic imports for large components
- Lazy loading of non-critical components

### Rendering Patterns
```typescript
// Dynamic imports for code splitting
const DynamicComponent = dynamic(
  () => import('./heavy-component'),
  { loading: () => <Skeleton /> }
);

// Memo for expensive computations
const MemoizedComponent = memo(({ data }) => {
  const processedData = useMemo(
    () => expensiveComputation(data),
    [data]
  );
  return <div>{processedData}</div>;
});
```

## Development Patterns

### Error Boundaries
Global error handling with React Error Boundaries:

```typescript
class ErrorBoundary extends Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true };
  }

  componentDidCatch(error, errorInfo) {
    console.error('Error boundary caught an error:', error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      return <ErrorFallback />;
    }
    return this.props.children;
  }
}
```

### Loading States
Consistent loading patterns across the application:

```typescript
// Skeleton loading
if (isLoading) return <Skeleton className="h-96 w-full" />;

// Component-level loading
{isLoading ? <LoadingSpinner /> : <ActualContent />}

// Suspense boundaries
<Suspense fallback={<PageSkeleton />}>
  <AsyncComponent />
</Suspense>
```

### Analytics Integration
PostHog integration for user analytics:

```typescript
const posthog = usePostHog();

const handleAction = () => {
  posthog.capture(AnalyticsEvent.STRATEGY_DOWNLOADED, {
    strategyId: strategy.id,
    userId: user.id,
  });
};
```

## Best Practices

### Code Organization
1. **Single Responsibility**: Each component has one clear purpose
2. **Composition over Inheritance**: Use component composition patterns
3. **Consistent Naming**: Clear, descriptive names for files and functions
4. **Export Strategy**: Use index.ts files for clean imports

### Type Safety
1. **Strict TypeScript**: No `any` types allowed
2. **Runtime Validation**: Zod schemas for external data
3. **Type Guards**: Custom type guards for type narrowing
4. **Generic Components**: Reusable components with proper typing

### Performance
1. **Lazy Loading**: Code splitting for large features
2. **Memoization**: React.memo and useMemo for expensive operations
3. **Query Optimization**: Efficient React Query usage
4. **Bundle Analysis**: Regular bundle size monitoring

### Accessibility
1. **Semantic HTML**: Proper HTML structure and semantics
2. **ARIA Labels**: Comprehensive ARIA support via Radix UI
3. **Keyboard Navigation**: Full keyboard accessibility
4. **Screen Reader Support**: Proper screen reader compatibility

### Testing Strategy
1. **Unit Tests**: Component and utility function testing
2. **Integration Tests**: Feature-level testing
3. **E2E Tests**: Critical user journey testing
4. **Type Testing**: TypeScript compiler as first line of defense

### Error Handling
1. **Graceful Degradation**: Fallback UI for errors
2. **User Feedback**: Clear error messages and recovery options
3. **Logging**: Comprehensive error logging and monitoring
4. **Retry Logic**: Automatic retry for transient failures

---

<!-- DOCUMENT_METADATA_END
This document has been optimized for LLM parsing and embedding generation with the following enhancements:
- Added semantic section markers (SECTION_START/SECTION_END) for better document chunking
- Enhanced context with detailed explanations and business context
- Structured information with consistent formatting patterns
- Added explicit relationships between concepts and technologies
- Included comprehensive keywords and metadata for better searchability
- Improved code example explanations with context and purpose
- Added detailed technology descriptions with use cases and benefits
- Enhanced architectural pattern explanations with implementation details
- Structured domain descriptions with business context and responsibilities
- Optimized for semantic search and knowledge extraction by LLMs
-->
