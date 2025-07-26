# Markit Frontend Style Guide

<!-- DOCUMENT_METADATA
Document Type: Development Style Guide and Code Standards
Project: Markit Frontend Application
Framework: Next.js 15 with React 19 and TypeScript
Purpose: Comprehensive coding standards, patterns, and best practices for consistent development
Scope: Frontend development guidelines, component patterns, and code organization
Last Updated: 2024
-->

<!-- KEYWORDS: Style-Guide, Code-Standards, TypeScript, React-Patterns, Component-Design, Coding-Best-Practices, Frontend-Guidelines, Markit -->

## Table of Contents
1. [General Principles](#general-principles) - Core development philosophy and coding principles
2. [File Naming Conventions](#file-naming-conventions) - Consistent file and directory naming standards
3. [TypeScript Guidelines](#typescript-guidelines) - Type definitions and TypeScript best practices
4. [Component Patterns](#component-patterns) - React component design patterns and structures
5. [Styling Guidelines](#styling-guidelines) - Tailwind CSS usage and styling conventions
6. [Form Handling Standards](#form-handling-standards) - Form validation and data handling patterns
7. [API and Data Layer](#api-and-data-layer) - Data fetching and API integration standards
8. [Constants and Enums](#constants-and-enums) - Application constants and enumeration patterns
9. [Import/Export Patterns](#importexport-patterns) - Module import/export organization standards
10. [Code Organization](#code-organization) - Project structure and file organization principles
11. [ESLint and Prettier Configuration](#eslint-and-prettier-configuration) - Code quality and formatting tools
12. [Best Practices](#best-practices) - Performance, accessibility, and development best practices

## General Principles

<!-- SECTION_START: Development Philosophy -->
**Overview**: The Markit frontend development follows established principles that prioritize code maintainability, type safety, and consistent patterns across the entire codebase.

### Core Development Philosophy

**Principle 1: Consistency Over Cleverness**
- **Purpose**: Maintain predictable code patterns that any team member can understand
- **Implementation**: Use established patterns rather than creative solutions
- **Benefits**: Reduced onboarding time, easier debugging, better maintainability
- **Examples**: Consistent component structure, standardized naming conventions, uniform API patterns

**Principle 2: Type Safety First**
- **Purpose**: Leverage TypeScript's type system to prevent runtime errors
- **Implementation**: Strict TypeScript configuration with comprehensive type coverage
- **Benefits**: Catch errors at compile time, better developer experience, self-documenting code
- **Examples**: Zod schema validation, typed API responses, strict function signatures

**Principle 3: Composition Over Inheritance**
- **Purpose**: Build flexible, reusable components through composition patterns
- **Implementation**: React composition patterns, polymorphic components, compound components
- **Benefits**: Better code reuse, flexible component APIs, easier testing
- **Examples**: Compound card components, polymorphic button with asChild prop, slot-based composition

**Principle 4: Functional Programming Approach**
- **Purpose**: Write predictable, testable code with minimal side effects
- **Implementation**: Pure functions, immutable data patterns, functional hooks
- **Benefits**: Easier testing, predictable behavior, better performance optimizations
- **Examples**: Pure utility functions, immutable state updates, functional form validation

**Principle 5: Domain-Driven Organization**
- **Purpose**: Organize code by business domains rather than technical layers
- **Implementation**: Domain-based folder structure, business-focused module organization
- **Benefits**: Better team collaboration, clearer ownership, business-aligned development
- **Examples**: Brief domain, user domain, strategy domain with clear boundaries

### Code Formatting Standards

**Indentation and Spacing Standards**:
- **Indentation**: Use exactly 2 spaces for all indentation (no tabs)
- **Purpose**: Consistent visual hierarchy and reduced file size
- **Application**: Applied to TypeScript, JavaScript, JSX, JSON, and CSS files

**String and Syntax Standards**:
- **Quotes**: Use double quotes for all string literals
- **Trailing Commas**: Include trailing commas in all multi-line structures
- **Semicolons**: Always include semicolons at the end of statements
- **Purpose**: Consistent formatting, easier diffs, reduced parsing errors

**Variable Declaration Standards**:
- **const**: Preferred for all immutable values and object references
- **let**: Used only when reassignment is necessary
- **var**: Never used (avoid function-scoped variables)
- **Purpose**: Block scoping, immutability by default, clearer intent

**Code Style Examples**:
```typescript
// ✅ Correct formatting
const userPreferences = {
  theme: "dark",
  language: "en",
  notifications: true, // trailing comma
};

const getUserById = async (id: string): Promise<User> => { // double quotes, semicolon
  const response = await api.get(`users/${id}`);
  return response.json();
};

// ❌ Incorrect formatting
var user_data = {
  theme: 'light', // single quotes
  language: 'en'  // missing trailing comma
}

function getUser(id) { // missing types, inconsistent style
  return api.get('users/' + id) // missing semicolon
}
```
<!-- SECTION_END: Development Philosophy -->

## File Naming Conventions

<!-- SECTION_START: File Naming Standards -->
**Overview**: Consistent file naming conventions create predictable project structure and improve developer experience across the Markit frontend codebase.

### File Naming Pattern Standards

**Naming Convention Rules by File Type**:

**Directory Names - kebab-case**
- **Pattern**: `kebab-case` (lowercase with hyphens)
- **Purpose**: Consistent URL-safe naming, easy navigation
- **Usage**: All directories, configuration files, and non-component files
- **Examples**: `brief-steps/`, `api-routes.ts`, `next.config.ts`

**React Component Files - PascalCase.tsx**
- **Pattern**: `PascalCase.tsx` (capitalized words, no separators)
- **Purpose**: Matches React component naming conventions
- **Usage**: All React components, pages, and UI elements
- **Examples**: `Button.tsx`, `UserProfile.tsx`, `BusinessInformationForm.tsx`

**Utility and Service Files - camelCase.ts**
- **Pattern**: `camelCase.ts` (first word lowercase, subsequent words capitalized)
- **Purpose**: Follows JavaScript function and variable naming conventions
- **Usage**: Utility functions, hooks, services, and business logic files
- **Examples**: `utils.ts`, `userHooks.ts`, `apiClient.ts`

**Barrel Export Files - index.ts**
- **Pattern**: Always named `index.ts` or `index.tsx`
- **Purpose**: Provides clean import paths and module boundaries
- **Usage**: Re-exporting modules, creating public APIs for directories
- **Examples**: `components/ui/index.ts`, `domains/brief/index.ts`

### Correct vs Incorrect Naming Examples

**✅ Correct File Naming Examples**:
```
components/ui/button.tsx              # UI component
components/shared/mobile-alert.tsx    # Shared component
modules/brief-steps/                  # Feature module directory
domains/user/hooks.ts                 # Domain hooks
constants/api-routes.ts               # API route constants
lib/utils.ts                         # Utility functions
config/env.ts                        # Configuration file
types/general.ts                     # Type definitions
middleware.ts                        # Next.js middleware
```

**❌ Incorrect File Naming Examples**:
```
components/ui/Button.tsx              # Should be button.tsx
modules/briefSteps/                   # Should be brief-steps/
domains/user/userHooks.ts            # Should be hooks.ts
constants/ApiRoutes.ts               # Should be api-routes.ts
lib/Utils.ts                         # Should be utils.ts
config/ENV.ts                        # Should be env.ts
types/General.ts                     # Should be general.ts
```

### Special File Naming Standards

**Standard Domain and Module Files**:

**index.ts - Barrel Export Files**
- **Purpose**: Provides clean import paths and defines public module APIs
- **Usage**: Re-export components, utilities, and types from a directory
- **Location**: Every directory that exports multiple items
- **Content**: Export statements for public module interface

**validation/index.ts - Form Validation Schemas**
- **Purpose**: Contains Zod schemas for form validation and type inference
- **Usage**: Form validation logic, data transformation schemas
- **Location**: Within feature modules that handle forms
- **Content**: Zod schemas, validation functions, inferred types

**constants.ts - Domain-Specific Constants**
- **Purpose**: Defines domain-specific constants, enums, and configuration
- **Usage**: Business logic constants, default values, enumeration definitions
- **Location**: Within each domain and feature module
- **Content**: Enums, constant objects, default values

**types.ts - Type Definitions**
- **Purpose**: Contains TypeScript interfaces and type definitions
- **Usage**: Domain data structures, API response types, component props
- **Location**: Domains, modules, and shared type directories
- **Content**: Interfaces, type aliases, generic types

**api.ts - HTTP Client Functions**
- **Purpose**: Contains HTTP client functions for server communication
- **Usage**: API endpoint calls, data fetching functions
- **Location**: Within each domain for domain-specific API calls
- **Content**: HTTP client functions, request/response handling

**queries.ts - React Query Hooks**
- **Purpose**: Contains React Query hooks for data fetching and caching
- **Usage**: Server state management, data synchronization
- **Location**: Within domains for data fetching logic
- **Content**: useQuery hooks, query key definitions

**mutations.ts - React Query Mutation Hooks**
- **Purpose**: Contains React Query mutation hooks for data modifications
- **Usage**: Server state updates, optimistic updates, error handling
- **Location**: Within domains for data modification logic
- **Content**: useMutation hooks, mutation functions, cache invalidation

### File Organization Benefits

**Predictable Structure Benefits**:
- **Developer Experience**: Easy to locate files based on naming patterns
- **IDE Integration**: Better autocomplete and file navigation
- **Team Collaboration**: Consistent expectations across team members
- **Tooling Support**: Better support from build tools and linters

**Naming Convention Benefits**:
- **Import Clarity**: Clear distinction between components and utilities
- **File Type Recognition**: Instant recognition of file purpose from name
- **URL Safety**: kebab-case ensures URL-safe directory names
- **Convention Alignment**: Matches React and TypeScript community standards
<!-- SECTION_END: File Naming Standards -->

## TypeScript Guidelines

<!-- SECTION_START: TypeScript Type System Standards -->
**Overview**: The Markit frontend uses TypeScript with strict configuration to ensure type safety, better developer experience, and runtime error prevention.

### Interface vs Type Usage Standards

**When to Use Interfaces**:
- **Purpose**: For object shapes that might be extended or implemented
- **Benefits**: Support inheritance, can be merged, better for OOP patterns
- **Use Cases**: Component props, domain entities, extendable data structures

**When to Use Type Aliases**:
- **Purpose**: For unions, intersections, primitives, and complex type compositions
- **Benefits**: More flexible, support computed types, better for functional patterns
- **Use Cases**: Union types, function signatures, computed types

**Interface Examples - Extensible Object Structures**:
```typescript
// ✅ Interface for extensible user entity
export interface User extends TimeStamps {
  id: Id;
  email: string;
  fullName: string;
  role: UserRole;
}

// ✅ Interface for component props that might be extended
export interface ButtonProps extends React.ComponentProps<"button"> {
  variant?: "default" | "outline" | "ghost";
  size?: "default" | "sm" | "lg";
  asChild?: boolean;
}

// ✅ Interface for domain entities with common patterns
export interface BusinessInformation extends TimeStamps {
  id: Id;
  name: string;
  website?: string;
  industry: string;
  model: BusinessModel;
  size: BusinessSize;
}
```

**Type Alias Examples - Unions and Complex Types**:
```typescript
// ✅ Type for union types and literals
export type Status = "pending" | "completed" | "failed";
export type Theme = "light" | "dark" | "system";

// ✅ Type for function signatures
export type EventHandler<T = Event> = (event: T) => void;
export type ValidationResult<T> = {
  success: boolean;
  data?: T;
  errors?: ValidationError[];
};

// ✅ Type for computed and conditional types
export type ApiResponse<T> = {
  data: T;
  message: string;
  success: boolean;
};
```

### Type Definition Standards

**Descriptive Type Naming Conventions**:
- **Form Values**: Suffix with `FormValues` for Zod-inferred form types
- **API Types**: Suffix with `Response`, `Request`, or `Body` for API-related types
- **Generic Types**: Use descriptive names that indicate the type's purpose
- **Domain Types**: Use business domain terminology rather than technical terms

**Type Definition Examples**:
```typescript
// ✅ Form type inferred from Zod schema
export type BusinessInformationFormValues = z.infer<typeof businessInformationFormSchema>;
export type CompetitorAnalysisFormValues = z.infer<typeof competitorAnalysisFormSchema>;

// ✅ API request/response types
export type CreateUserRequest = {
  email: string;
  password: string;
  fullName: string;
};

export type GetStrategyResponse = {
  strategy: Strategy;
  metadata: StrategyMetadata;
};

// ✅ Generic utility types
export type TimeStamps = {
  createdAt: string;
  updatedAt: string;
};

export type WithOptional<T, K extends keyof T> = Omit<T, K> & Partial<Pick<T, K>>;

// ✅ Branded types for type safety
export type Id = number & { readonly brand: unique symbol };
export type Email = string & { readonly brand: unique symbol };
```

### Function Type Standards

**Component Props Function Patterns**:
```typescript
// ✅ Interface for React component props with proper inheritance
interface ButtonProps extends React.ComponentProps<"button"> {
  variant?: "default" | "outline" | "ghost" | "destructive";
  size?: "default" | "sm" | "lg" | "icon";
  asChild?: boolean;
  isLoading?: boolean;
}

// ✅ Interface for form field components
interface FormFieldProps {
  name: string;
  label: string;
  placeholder?: string;
  disabled?: boolean;
  required?: boolean;
}

// ✅ Interface for polymorphic component props
interface PolymorphicProps<T extends React.ElementType> {
  as?: T;
  children: React.ReactNode;
}
```

**Utility Function Type Patterns**:
```typescript
// ✅ Explicit return types for utility functions
export const cn = (...inputs: ClassValue[]): string => {
  return twMerge(clsx(inputs));
};

export const formatCurrency = (amount: number, currency = "USD"): string => {
  return new Intl.NumberFormat("en-US", {
    style: "currency",
    currency,
  }).format(amount);
};

// ✅ Generic utility functions with constraints
export const pick = <T, K extends keyof T>(
  obj: T,
  keys: K[]
): Pick<T, K> => {
  const result = {} as Pick<T, K>;
  keys.forEach(key => {
    result[key] = obj[key];
  });
  return result;
};
```

**API Function Type Patterns**:
```typescript
// ✅ Async API functions with proper error handling
export const getBusinessInformation = async (): Promise<BusinessInformation> => {
  try {
    const response = await api.get(apiRoutes.brief.businessInformation);
    return response.json<BusinessInformation>();
  } catch (error) {
    throw new ApiError("Failed to fetch business information", error);
  }
};

export const createStrategy = async (
  data: CreateStrategyRequest
): Promise<Strategy> => {
  return api.post(apiRoutes.strategy.create, { json: data }).json<Strategy>();
};
```

### Advanced TypeScript Patterns

**Conditional Types for API Responses**:
```typescript
// ✅ Conditional types for different response states
export type ApiState<T> = 
  | { status: "loading"; data: null; error: null }
  | { status: "success"; data: T; error: null }
  | { status: "error"; data: null; error: string };

// ✅ Mapped types for form validation
export type ValidationErrors<T> = {
  [K in keyof T]?: string[];
};
```

**Strict Type Configuration Benefits**:
- **Compile-Time Safety**: Catch type errors before runtime
- **IDE Support**: Better autocomplete, refactoring, and navigation
- **Self-Documenting Code**: Types serve as inline documentation
- **Refactoring Confidence**: Safe refactoring with type checking
- **Team Collaboration**: Clear contracts between different parts of the codebase
<!-- SECTION_END: TypeScript Type System Standards -->

## Component Patterns

### Component Structure
```typescript
// ✅ Standard component pattern
import * as React from "react";
import { cn } from "@/lib/utils";

interface ComponentProps extends React.ComponentProps<"div"> {
  variant?: "default" | "secondary";
  children: React.ReactNode;
}

export const Component = React.forwardRef<HTMLDivElement, ComponentProps>(
  ({ className, variant = "default", children, ...props }, ref) => {
    return (
      <div
        ref={ref}
        className={cn("base-classes", variantClasses[variant], className)}
        {...props}
      >
        {children}
      </div>
    );
  }
);

Component.displayName = "Component";
```

### Form Field Components
```typescript
// ✅ Form field pattern
export const NameField = () => {
  const form = useFormContext<BusinessInformationFormValues>();

  return (
    <FormField
      control={form.control}
      name="name"
      render={({ field }) => (
        <FormItem>
          <FormLabel>Name</FormLabel>
          <FormControl>
            <Input
              {...field}
              placeholder="Acme Inc."
              disabled={form.formState.disabled}
            />
          </FormControl>
          <FormMessage />
        </FormItem>
      )}
    />
  );
};
```

### Compound Components
```typescript
// ✅ Compound component pattern
function Card({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="card"
      className={cn("base-card-classes", className)}
      {...props}
    />
  );
}

function CardHeader({ className, ...props }: React.ComponentProps<"div">) {
  return (
    <div
      data-slot="card-header"
      className={cn("card-header-classes", className)}
      {...props}
    />
  );
}

// Export pattern
export { Card, CardHeader, CardContent, CardFooter };
```

### Polymorphic Components (asChild pattern)
```typescript
// ✅ Polymorphic component with Slot
function Button({ 
  className, 
  variant, 
  size, 
  asChild = false, 
  ...props 
}: ButtonProps) {
  const Comp = asChild ? Slot : "button";
  
  return (
    <Comp
      data-slot="button"
      className={cn(buttonVariants({ variant, size, className }))}
      {...props}
    />
  );
}
```

## Styling Guidelines

### Tailwind CSS Usage

#### Class Organization
```typescript
// ✅ Good - grouped by purpose with logical order
className={cn(
  // Layout & positioning
  "inline-flex items-center justify-center",
  // Spacing
  "gap-2 px-4 py-2.5",
  // Typography
  "text-sm font-bold whitespace-nowrap",
  // Visual styling
  "rounded border bg-background",
  // States & interactions
  "hover:bg-accent focus-visible:ring-2",
  // Responsive & accessibility
  "disabled:opacity-50 aria-invalid:border-destructive",
  // Custom/conditional classes
  className
)}

// ❌ Bad - random order, hard to read
className="text-sm px-4 inline-flex rounded hover:bg-accent disabled:opacity-50 items-center"
```

#### Custom CSS Variables
```css
/* ✅ Use semantic color names */
:root {
  --primary: rgba(114, 141, 87, 1);
  --primary-foreground: rgba(250, 250, 250, 1);
  --muted-foreground: oklch(0.552 0.016 285.938);
}

/* ✅ Use consistent spacing scale */
--radius: 0.625rem;
--radius-sm: calc(var(--radius) - 4px);
--radius-lg: var(--radius);
```

#### Class Variance Authority (CVA)
```typescript
// ✅ Use CVA for component variants
const buttonVariants = cva(
  // Base classes - always applied
  "inline-flex items-center justify-center rounded text-sm font-bold transition-all",
  {
    variants: {
      variant: {
        default: "bg-primary text-primary-foreground hover:bg-primary/90",
        outline: "border bg-background hover:bg-accent",
        ghost: "hover:bg-accent hover:text-accent-foreground",
      },
      size: {
        default: "h-10 px-4 py-2.5",
        sm: "h-9 px-3 py-2",
        lg: "h-11 px-8 py-3",
      },
    },
    defaultVariants: {
      variant: "default",
      size: "default",
    },
  }
);
```

#### Responsive Design
```typescript
// ✅ Mobile-first responsive classes
className="flex flex-col gap-4 md:flex-row md:gap-6 lg:gap-8"

// ✅ Hide on mobile, show on desktop
className="hidden lg:block"

// ✅ Responsive typography
className="text-base md:text-lg lg:text-xl"
```

#### Dark Mode Support
```typescript
// ✅ Use CSS variables for theme-aware colors
className="bg-background text-foreground border-border"

// ✅ When direct dark mode classes needed
className="bg-white dark:bg-gray-900 text-gray-900 dark:text-white"
```

### Typography System
```typescript
// ✅ Consistent typography components
export const TypographyH1 = ({ children, className }: TypographyProps) => (
  <h1 className={cn("text-[32px] font-bold", className)}>
    {children}
  </h1>
);

export const TypographyH2 = ({ children, className }: TypographyProps) => (
  <h2 className={cn("text-[28px] font-bold", className)}>
    {children}
  </h2>
);

export const Subtitle = ({ children, className }: TypographyProps) => (
  <h2 className={cn("text-muted-foreground text-base font-medium", className)}>
    {children}
  </h2>
);
```

## Form Handling Standards

### Validation Schema Pattern
```typescript
// ✅ Zod schema with clear error messages
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

// ✅ Infer types from schema
export type BusinessInformationFormValues = z.infer<typeof businessInformationFormSchema>;
```

### Form Component Structure
```typescript
// ✅ Form component pattern
export const BusinessInformationForm = () => {
  const form = useForm<BusinessInformationFormValues>({
    resolver: zodResolver(businessInformationFormSchema),
    defaultValues: {
      name: "",
      website: "",
      // ... other defaults
    },
  });

  const onSubmit = (values: BusinessInformationFormValues) => {
    // Handle form submission
  };

  return (
    <Form {...form}>
      <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-6">
        <NameField />
        <WebsiteField />
        {/* Other fields */}
        <Button type="submit">Submit</Button>
      </form>
    </Form>
  );
};
```

### Error Handling
```typescript
// ✅ Consistent error message patterns
{
  message: "Name is required"           // Required fields
  message: "Please enter a valid URL"   // Format validation  
  message: "At least one item is required" // Array validation
  message: "Password must be at least 8 characters" // Length validation
}
```

## API and Data Layer

### API Route Constants
```typescript
// ✅ Nested object structure for organization
export const apiRoutes = {
  auth: {
    signIn: "auth/sign-in",
    signUp: "auth/sign-up",
    verifyEmail: "auth/verify-email",
  },
  brief: {
    businessInformation: "brief/business-informations",
    getById: (id: string) => `brief/${id}`,
  },
  strategy: {
    getByUserId: "strategy/user",
    download: (id: string) => `strategy/download/${id}`,
  },
};
```

### React Query Patterns
```typescript
// ✅ Query hook pattern
export const useGetBusinessInformationQuery = () =>
  useQuery({
    queryKey: businessInformationQueryKeys.details(),
    queryFn: getBusinessInformation,
  });

// ✅ Mutation hook pattern
export const useCreateBusinessInformationMutation = () =>
  useMutation({
    mutationFn: createBusinessInformation,
    onSuccess: () => {
      queryClient.invalidateQueries({
        queryKey: businessInformationQueryKeys.all,
      });
    },
  });

// ✅ Query key constants
export const businessInformationQueryKeys = {
  all: ["businessInformation"] as const,
  details: () => [...businessInformationQueryKeys.all, "details"] as const,
  list: (params: ListParams) => [...businessInformationQueryKeys.all, "list", params] as const,
};
```

### API Client Functions
```typescript
// ✅ API function pattern
export const getBusinessInformation = async (): Promise<BusinessInformation> => {
  return api.get(apiRoutes.brief.businessInformation).json<BusinessInformation>();
};

export const createBusinessInformation = async (
  data: BusinessInformationBody
): Promise<BusinessInformation> => {
  return api.post(apiRoutes.brief.businessInformation, { json: data }).json<BusinessInformation>();
};
```

## Constants and Enums

### Enum Definitions
```typescript
// ✅ Use PascalCase for enum names, camelCase for values
export enum MarketingStrategy {
  NeedsImprovement = "needsImprovement",
  StartingFromScratch = "startingFromScratch", 
  WorksWell = "worksWell",
}

export enum IdealCustomer {
  Business = "business",
  Individual = "individual",
}

// ✅ Use enum for TypeScript, string literals for API values
export enum StrategyStatus {
  Pending = "pending",
  Opened = "opened", 
  Edited = "edited",
  Completed = "completed",
}
```

### Constant Objects
```typescript
// ✅ Use const assertions for immutable objects
export const routes = {
  signIn: "/sign-in",
  signUp: "/sign-up",
  dashboard: "/dashboard",
  briefStep: (step: BriefFormSteps) => `/brief/${step}`,
  expertBrief: (id: string) => `/expert/briefs/${id}`,
} as const;

// ✅ Mapping objects for UI logic
export const stepsToPercentage = {
  [BriefFormSteps.BusinessInformation]: 16,
  [BriefFormSteps.MarketingGoals]: 33,
  [BriefFormSteps.TargetAudience]: 50,
  // ... other mappings
} as const;
```

### General Constants
```typescript
// ✅ Use SCREAMING_SNAKE_CASE for primitive constants
export const OTHER = "other";
export const MAX_FILE_SIZE = 5 * 1024 * 1024; // 5MB
export const API_TIMEOUT = 30000; // 30 seconds

// ✅ Group related constants
export const VALIDATION_MESSAGES = {
  REQUIRED: "This field is required",
  INVALID_EMAIL: "Please enter a valid email address",
  PASSWORD_TOO_SHORT: "Password must be at least 8 characters long",
} as const;
```

## Import/Export Patterns

### Import Organization
```typescript
// ✅ Import order and grouping
// 1. React and external libraries
import * as React from "react";
import { useQuery } from "@tanstack/react-query";
import { z } from "zod";

// 2. Internal UI components (alphabetical)
import { Button } from "@/components/ui/button";
import { Form, FormControl, FormField } from "@/components/ui/form";
import { Input } from "@/components/ui/input";

// 3. Internal utilities and services
import { cn } from "@/lib/utils";
import { api } from "@/config/api";

// 4. Types and constants
import type { BusinessInformation } from "@/domains/brief/business-information";
import { businessInformationQueryKeys } from "./constants";

// 5. Relative imports last
import { BusinessInformationFormValues } from "./validation";
```

### Export Patterns
```typescript
// ✅ Named exports for most components
export const Button = () => { /* ... */ };
export const Card = () => { /* ... */ };

// ✅ Default exports only for pages and main modules
export default function HomePage() { /* ... */ }

// ✅ Barrel exports in index.ts files
export { Button } from "./button";
export { Card, CardHeader, CardContent } from "./card";
export { Input } from "./input";

// ✅ Re-export types and constants
export type { ButtonProps } from "./button";
export { buttonVariants } from "./button";
```

### Path Aliases
```typescript
// ✅ Use consistent path aliases
import { Button } from "@/components/ui/button";
import { useUserStore } from "@/domains/user";
import { routes } from "@/constants/routes";
import { cn } from "@/lib/utils";

// ❌ Avoid relative imports for commonly used modules
import { Button } from "../../../components/ui/button";
```

## Code Organization

### Domain Structure
```
domains/[domain]/
├── index.ts              # Public exports
├── api.ts               # API functions
├── constants.ts         # Domain constants
├── types.ts            # Type definitions
├── queries.ts          # React Query hooks
├── mutations.ts        # Mutation hooks
└── [subdomain]/        # Nested domains
    ├── index.ts
    ├── api.ts
    ├── constants.ts
    └── types.ts
```

### Module Structure
```
modules/[feature]/
├── index.tsx           # Main feature component
├── components/         # Feature-specific components
│   ├── index.ts       # Component exports
│   └── [component].tsx
├── constants/         # Feature constants
│   └── index.ts
├── validation/        # Form schemas
│   └── index.ts
└── utils/            # Feature utilities
    └── index.ts
```

### Component Structure
```
components/
├── ui/                # Design system components
│   ├── button.tsx
│   ├── card.tsx
│   └── index.ts      # Barrel exports
└── shared/           # Business logic components
    ├── header.tsx
    ├── mobile-alert.tsx
    └── index.ts
```

## ESLint and Prettier Configuration

### ESLint Rules
```javascript
// ✅ Extend Next.js recommended configs
const eslintConfig = [
  ...compat.extends("next/core-web-vitals", "next/typescript"),
];
```

### Prettier Configuration
```json
{
  "plugins": ["prettier-plugin-tailwindcss"]
}
```

### Auto-formatting Rules
- **Tailwind classes**: Automatically sorted by prettier-plugin-tailwindcss
- **Imports**: Manually organized by category
- **Trailing commas**: Always included in multi-line structures
- **Semicolons**: Always required
- **Quotes**: Double quotes for strings

## Best Practices

### Performance
```typescript
// ✅ Use React.memo for expensive components
export const ExpensiveComponent = React.memo(({ data }: Props) => {
  const processedData = React.useMemo(
    () => expensiveComputation(data),
    [data]
  );
  
  return <div>{processedData}</div>;
});

// ✅ Use dynamic imports for code splitting
const HeavyComponent = React.lazy(() => import("./heavy-component"));

// ✅ Optimize React Query with selective invalidation
const { mutate } = useMutation({
  mutationFn: updateUser,
  onSuccess: (data) => {
    queryClient.setQueryData(userQueryKeys.details(data.id), data);
    queryClient.invalidateQueries({ queryKey: userQueryKeys.lists() });
  },
});
```

### Accessibility
```typescript
// ✅ Use semantic HTML elements
<main>
  <section>
    <h1>Page Title</h1>
    <article>Content</article>
  </section>
</main>

// ✅ Include ARIA attributes when needed
<button
  aria-expanded={isOpen}
  aria-controls="menu"
  aria-label="Toggle navigation menu"
>
  Menu
</button>

// ✅ Use data-slot for component identification
<div data-slot="card" className="...">
```

### Error Handling
```typescript
// ✅ Graceful error handling in components
if (isLoading) return <Skeleton className="h-96 w-full" />;
if (error) return <ErrorMessage error={error} />;
if (!data) return <EmptyState />;

// ✅ Error boundaries for component trees
<ErrorBoundary fallback={<ErrorFallback />}>
  <SuspiciousComponent />
</ErrorBoundary>

// ✅ API error handling
hooks: {
  beforeError: [
    async (error) => {
      if (error.response.status === 401) {
        useUserStore.getState().setUser(null);
        window.location.href = routes.signIn;
      }
      return error;
    },
  ],
}
```

### State Management
```typescript
// ✅ Use Zustand for client state
export const useUserStore = create<UserStore>()(
  persist(
    (set) => ({
      user: null,
      setUser: (user: User | null) => set({ user }),
    }),
    {
      name: "user-storage",
      storage: createJSONStorage(() => localStorage),
    }
  )
);

// ✅ Use React Query for server state
const { data, isLoading, error } = useQuery({
  queryKey: userQueryKeys.details(userId),
  queryFn: () => getUser(userId),
  enabled: !!userId,
});

// ✅ Use local state for component-specific UI state
const [isOpen, setIsOpen] = React.useState(false);
const [searchTerm, setSearchTerm] = React.useState("");
```

### Testing Considerations
```typescript
// ✅ Use data-testid for testing
<button data-testid="submit-button">Submit</button>

// ✅ Export test utilities
export const createMockUser = (overrides?: Partial<User>): User => ({
  id: 1,
  email: "test@example.com",
  fullName: "Test User",
  ...overrides,
});

// ✅ Separate business logic for easier testing
export const validateBusinessInformation = (data: BusinessInformationInput) => {
  // Pure function that can be tested independently
  return businessInformationFormSchema.safeParse(data);
};
```

---

<!-- DOCUMENT_METADATA_END
This style guide has been optimized for LLM parsing and embedding generation with the following enhancements:
- Added comprehensive document metadata and keywords for better searchability
- Enhanced section markers (SECTION_START/SECTION_END) for improved document chunking
- Structured information with detailed explanations and context for each coding standard
- Added explicit purpose, implementation, and benefits for each guideline
- Included comprehensive code examples with detailed explanations
- Enhanced naming convention standards with clear use cases and examples
- Improved TypeScript guideline explanations with advanced patterns and best practices
- Added detailed context for when and why to use specific patterns
- Structured best practices with clear categorization and implementation guidance
- Optimized for semantic search and knowledge extraction by AI systems
- Enhanced code quality standards with rationale and business context
- Improved readability and parsing for automated documentation systems
-->