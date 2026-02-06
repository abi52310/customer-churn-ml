📄 ML Column Types Cheat Sheet
📌 Purpose

Quick reference to identify and handle different column types in ML pipelines.

🧠 Column Type Taxonomy (Production ML View)

In real ML systems, columns are typically classified into:

Numeric

Categorical (Nominal)

Ordinal (Ordered categorical)

Boolean / Binary

Identifier

Datetime / Temporal

Text / Unstructured

Derived / Engineered Features

🏆 1. Numeric Columns

Definition:
Numbers where mathematical operations are meaningful.

Ask Yourself:

Can I add / subtract meaningfully?

Does magnitude matter?

Examples:

Age

Salary

MonthlyCharges

TransactionAmount

Temperature

ML Treatment:

Scaling (StandardScaler, MinMaxScaler)

Outlier handling

Log transformation (optional)

🏆 2. Categorical Columns (Nominal)

Definition:
Labels with NO inherent order.

Ask Yourself:

Is this just a label or category?

Examples:

Gender

City

PaymentMethod

InternetService

ProductCategory

ML Treatment:

One Hot Encoding

Target Encoding (advanced use cases)

🏆 3. Ordinal Columns (Ordered Category)

Definition:
Categories with order but no numeric distance meaning.

Ask Yourself:

Does order matter?

But numeric difference does NOT matter?

Examples:

Low / Medium / High

Bronze / Silver / Gold

Education Level

Risk Level

ML Treatment:

Ordinal Encoding

Custom Mapping

🏆 4. Boolean / Binary Columns

Definition:
Two-state variable.

Examples:

Yes / No

True / False

0 / 1

ML Treatment:
Convert to numeric 0 / 1.

🏆 5. Identifier Columns (⚠ Usually Drop)

Definition:
Uniquely identifies an entity.

Examples:

CustomerID

MobileNumber

Email

AccountNumber

TransactionID

ML Treatment:
Usually DROP before modeling.
Keep only for joins, tracking, or audit.

🏆 6. Datetime / Temporal Columns

Definition:
Time-related columns.

Examples:

SignupDate

TransactionTime

LastLoginDate

ML Treatment:
Extract features such as:

Day of week

Month

Time since last event

Seasonality indicators

🏆 7. Text / Unstructured Columns

Definition:
Free-form text data.

Examples:

Customer complaints

Reviews

Support tickets

ML Treatment:

TF-IDF

Embeddings

NLP / LLM processing

🏆 8. Derived / Engineered Features

Definition:
Features created from raw columns.

Examples:

ChargesPerMonth = TotalCharges / tenure

CustomerLifetimeValue

DaysSinceLastLogin

⭐ Special Cases
High Cardinality Categorical

Examples:

Zipcode

ProductID

MerchantID

Requires special encoding strategies.

Numeric-Looking But Actually Categorical

Examples:

Rating (1–5)

SeniorCitizen (0/1 flag)

Treat based on meaning, not dtype.

🧠 Real World Column Classification Flow
1. Is value unique per row?
   YES → Identifier → Usually Drop

2. Is column time related?
   YES → Datetime / Temporal

3. Do numeric operations make sense?
   YES → Numeric

4. Does order exist but math doesn't?
   YES → Ordinal

5. Otherwise
   → Categorical

🏆 Telco Churn Dataset Example Mapping

Numeric

tenure

MonthlyCharges

TotalCharges

Categorical

Most service and demographic columns

Identifier

customerID

Binary

Churn

SeniorCitizen (context dependent)

⭐ Memory Shortcut
Type	Quick Meaning
Numeric	Math works
Categorical	Label only
Ordinal	Order matters
Binary	Two states
Identifier	Unique → Drop
Datetime	Time → Extract features
Text	Needs NLP
Derived	Created by you
🧠 Key Industry Principle

Never rely only on pandas dtype.
Always combine:

Domain knowledge

Data profiling

Schema contracts

📌 Recommended Usage

Use this sheet when:

Designing feature pipelines

Writing data contracts

Building cleaning configs

Reviewing new datasets