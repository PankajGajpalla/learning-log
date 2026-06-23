# The Complete AI/ML Engineer Curriculum — Master Reference

A searchable, hierarchical index of **every topic, subtopic, tool, technique, and concept** you'll encounter on the path to becoming an AI/ML engineer. Use **Ctrl+F** / **Cmd+F** to find anything instantly.

---

## How to Use This Document

1. **This is a reference, not a checklist to complete linearly.** You won't master everything here, and you don't need to.
2. **Priority tags:**
   - 🔴 **Essential** — you cannot skip this
   - 🟡 **Important** — most ML engineers know this
   - 🟢 **Specialized** — depends on your track
   - 🔵 **Advanced** — for going deeper, research, or seniority
3. **Use checkboxes** to track what you've covered.
4. **Don't panic at the size.** Even senior ML engineers don't know all of this — they know their core deeply and recognize the rest.

---

## Table of Contents

- [Part 1: Programming Foundations](#part-1-programming-foundations)
- [Part 2: Mathematics](#part-2-mathematics)
- [Part 3: Data Engineering for ML](#part-3-data-engineering-for-ml)
- [Part 4: Classical Machine Learning](#part-4-classical-machine-learning)
- [Part 5: Deep Learning](#part-5-deep-learning)
- [Part 6: NLP & Large Language Models](#part-6-nlp--large-language-models)
- [Part 7: Computer Vision](#part-7-computer-vision)
- [Part 8: Reinforcement Learning](#part-8-reinforcement-learning)
- [Part 9: MLOps & Production](#part-9-mlops--production)
- [Part 10: Advanced & Adjacent](#part-10-advanced--adjacent)
- [Part 11: Career & Soft Skills](#part-11-career--soft-skills)

---

# Part 1: Programming Foundations

## 1.1 Python Core 🔴

### Setup & Environment
- [ ] Installing Python (pyenv, conda, system Python — when to use which)
- [ ] Virtual environments: `venv`, `virtualenv`, `conda env`, `poetry`, `uv`, `pipenv`
- [ ] Package management: `pip`, `conda`, `poetry`, `uv`
- [ ] `requirements.txt` vs `pyproject.toml` vs `environment.yml`
- [ ] IDE setup: VS Code, PyCharm, Jupyter, JupyterLab
- [ ] REPL tools: ipython, ptpython

### Language Fundamentals
- [ ] Variables, naming conventions (snake_case, PEP 8)
- [ ] Data types: int, float, complex, bool, str, bytes, None
- [ ] Operators: arithmetic, comparison, logical, bitwise, identity, membership
- [ ] Type conversion and casting
- [ ] String formatting: f-strings, `.format()`, `%` (avoid), `repr`
- [ ] String methods: `split`, `join`, `strip`, `replace`, `startswith`, `find`
- [ ] Control flow: `if`/`elif`/`else`, ternary expressions
- [ ] Loops: `for`, `while`, `break`, `continue`, `else` clause on loops
- [ ] `match`/`case` (structural pattern matching, Python 3.10+)

### Data Structures
- [ ] Lists: methods, slicing, comprehensions
- [ ] Tuples: immutability, named tuples
- [ ] Dictionaries: methods, comprehensions, `dict.get()`, `setdefault`
- [ ] Sets and frozensets
- [ ] `collections` module: `Counter`, `defaultdict`, `OrderedDict`, `deque`, `namedtuple`, `ChainMap`
- [ ] `dataclasses`
- [ ] `enum` and `IntEnum`
- [ ] Hashing and mutability

### Functions
- [ ] Function definition, return values
- [ ] Positional, keyword, default arguments
- [ ] `*args`, `**kwargs`
- [ ] Keyword-only and positional-only arguments
- [ ] Type hints (`typing` module: `List`, `Dict`, `Optional`, `Union`, `Callable`, `Any`, `TypeVar`, `Generic`)
- [ ] `Protocol` and structural typing
- [ ] Lambda functions
- [ ] Closures and `nonlocal`
- [ ] Recursion and tail call considerations
- [ ] Scope: LEGB rule (Local, Enclosing, Global, Built-in)
- [ ] First-class functions, higher-order functions

### Object-Oriented Programming
- [ ] Classes, instances, `self`
- [ ] `__init__`, `__new__`
- [ ] Instance, class, static methods
- [ ] Inheritance: single, multiple, MRO (Method Resolution Order)
- [ ] `super()`
- [ ] Abstract base classes (`abc` module)
- [ ] Composition vs inheritance
- [ ] Magic / dunder methods: `__str__`, `__repr__`, `__eq__`, `__hash__`, `__len__`, `__iter__`, `__next__`, `__getitem__`, `__setitem__`, `__call__`, `__enter__`, `__exit__`, `__add__`, etc.
- [ ] Properties: `@property`, getter/setter
- [ ] Descriptors
- [ ] Metaclasses 🔵
- [ ] `__slots__` for memory optimization

### Advanced Language Features
- [ ] Decorators: function, class, parameterized, stacking
- [ ] `functools`: `wraps`, `lru_cache`, `partial`, `reduce`, `cache`
- [ ] Generators: `yield`, `yield from`, generator expressions
- [ ] Iterators: `iter`, `next`, custom iterators
- [ ] `itertools`: `chain`, `cycle`, `combinations`, `permutations`, `product`, `groupby`, `islice`, `takewhile`
- [ ] Context managers: `with`, `__enter__`/`__exit__`, `contextlib.contextmanager`
- [ ] Comprehensions: list, dict, set, generator
- [ ] Walrus operator `:=`

### Concurrency & Async
- [ ] Threading: `threading` module, `Thread`, `Lock`, `Event`
- [ ] Multiprocessing: `multiprocessing`, `Pool`, `Process`, `Queue`
- [ ] GIL (Global Interpreter Lock) — understand its implications
- [ ] `concurrent.futures`: `ThreadPoolExecutor`, `ProcessPoolExecutor`
- [ ] Async basics: `async`/`await`, coroutines
- [ ] `asyncio`: event loop, `gather`, `create_task`, `sleep`, `wait`
- [ ] `httpx`, `aiohttp` for async HTTP
- [ ] When to use async vs threads vs processes

### Error Handling
- [ ] `try`/`except`/`else`/`finally`
- [ ] Built-in exceptions hierarchy
- [ ] Custom exceptions
- [ ] Exception chaining (`raise ... from ...`)
- [ ] `assert` statements (and when not to use them)
- [ ] Logging vs printing: `logging` module, levels, handlers, formatters

### File I/O and Data Formats
- [ ] File handling: `open`, modes, `with`
- [ ] `pathlib` (modern, preferred over `os.path`)
- [ ] JSON: `json.dump`, `json.load`
- [ ] CSV: `csv` module
- [ ] Pickle: `pickle.dump`/`load` (and security concerns)
- [ ] YAML: `pyyaml`
- [ ] TOML: `tomllib` (3.11+) / `tomli`
- [ ] Parquet, Arrow (later, via pandas/polars)

### Standard Library Highlights
- [ ] `os`, `sys`, `pathlib`, `shutil`, `glob`
- [ ] `datetime`, `time`, `calendar`, `zoneinfo`
- [ ] `re` (regular expressions)
- [ ] `subprocess` for running external commands
- [ ] `argparse` for CLI arguments
- [ ] `random` and `secrets`
- [ ] `math`, `statistics`
- [ ] `urllib`, `http`

### Code Quality & Tooling
- [ ] Formatters: `black`, `ruff format`
- [ ] Linters: `ruff`, `flake8`, `pylint`
- [ ] Type checkers: `mypy`, `pyright`
- [ ] Import sorting: `isort` (now in `ruff`)
- [ ] Pre-commit hooks: `pre-commit` framework
- [ ] Docstrings: Google, NumPy, reStructuredText styles

### Testing
- [ ] `pytest`: test functions, fixtures, parametrization
- [ ] `unittest` (older, still common)
- [ ] Mocking: `unittest.mock`, `pytest-mock`
- [ ] Coverage: `pytest-cov`, `coverage.py`
- [ ] Property-based testing: `hypothesis`
- [ ] Test organization, test doubles, integration vs unit tests

### Performance & Profiling
- [ ] `cProfile`, `profile`
- [ ] `line_profiler`
- [ ] `memory_profiler`
- [ ] `timeit`
- [ ] When to optimize, when not to
- [ ] C extensions: `cython`, `numba` (just-in-time compilation)
- [ ] PyPy alternative interpreter

### Packaging
- [ ] `pyproject.toml`
- [ ] Building wheels and sdists
- [ ] Publishing to PyPI
- [ ] Semantic versioning

## 1.2 Software Engineering Basics 🔴

- [ ] Git: clone, add, commit, push, pull, fetch
- [ ] Git: branching, merging, rebasing, cherry-picking
- [ ] Git: stash, reset, revert, reflog
- [ ] Git: resolving merge conflicts
- [ ] GitHub/GitLab: pull requests, code review, issues
- [ ] `.gitignore`, `.gitattributes`
- [ ] Linux/Unix CLI: navigation (`cd`, `ls`, `pwd`), file ops (`cp`, `mv`, `rm`, `mkdir`)
- [ ] Linux/Unix CLI: `grep`, `sed`, `awk`, `find`, `xargs`
- [ ] Linux/Unix CLI: pipes, redirection, `tee`
- [ ] Process management: `ps`, `top`, `htop`, `kill`, `&`, `nohup`
- [ ] SSH, key generation, port forwarding
- [ ] tmux or screen for persistent sessions
- [ ] Bash scripting basics
- [ ] Code design principles: SOLID, DRY, KISS, YAGNI
- [ ] Design patterns (just the common ones: factory, singleton, observer, strategy)
- [ ] Refactoring techniques
- [ ] Reading other people's code

---

# Part 2: Mathematics

## 2.1 Linear Algebra 🔴

### Vectors
- [ ] Vectors: definition, geometric and algebraic views
- [ ] Vector addition, scalar multiplication
- [ ] Dot product (inner product)
- [ ] Cross product
- [ ] Vector norms: L0 (count), L1 (Manhattan), L2 (Euclidean), L-infinity, p-norms
- [ ] Unit vectors, normalization
- [ ] Angle between vectors, cosine similarity
- [ ] Vector projection

### Matrices
- [ ] Matrix as a collection of vectors
- [ ] Matrix as a linear transformation (CRITICAL intuition)
- [ ] Matrix multiplication (and why it's defined that way)
- [ ] Transpose, conjugate transpose
- [ ] Identity matrix
- [ ] Inverse matrix, conditions for invertibility
- [ ] Determinant: meaning, computation
- [ ] Trace
- [ ] Special matrices: diagonal, triangular, symmetric, skew-symmetric, orthogonal, unitary, positive definite, sparse

### Vector Spaces & Linear Maps
- [ ] Vector space axioms
- [ ] Subspaces, span
- [ ] Linear independence, basis, dimension
- [ ] Rank of a matrix
- [ ] Null space, column space, row space
- [ ] Rank-nullity theorem
- [ ] Linear transformations and their matrices
- [ ] Change of basis

### Solving Linear Systems
- [ ] Ax = b: existence and uniqueness
- [ ] Gaussian elimination, row echelon form
- [ ] LU decomposition
- [ ] Least squares (normal equations)

### Decompositions
- [ ] LU decomposition
- [ ] QR decomposition (Gram-Schmidt)
- [ ] Cholesky decomposition
- [ ] Eigendecomposition: eigenvalues, eigenvectors
- [ ] Diagonalization
- [ ] Singular Value Decomposition (SVD) — THE most important
- [ ] Spectral theorem
- [ ] PCA from SVD

### Advanced / Applied
- [ ] Quadratic forms
- [ ] Positive definite / semi-definite matrices
- [ ] Matrix calculus: derivatives of scalar/vector/matrix w.r.t. scalar/vector/matrix
- [ ] Kronecker product, Hadamard product
- [ ] Pseudo-inverse (Moore-Penrose)
- [ ] Tensor basics (generalization of matrices)

## 2.2 Calculus 🔴

### Single-Variable
- [ ] Limits, continuity
- [ ] Derivative definition (limit form)
- [ ] Derivative rules: power, product, quotient, chain
- [ ] Common derivatives: polynomials, exp, log, trig
- [ ] Higher-order derivatives
- [ ] Critical points, local/global extrema
- [ ] Mean value theorem
- [ ] Taylor series and approximations
- [ ] L'Hôpital's rule

### Integration
- [ ] Indefinite and definite integrals
- [ ] Fundamental theorem of calculus
- [ ] Integration techniques: substitution, by parts, partial fractions
- [ ] Improper integrals (used in probability)

### Multivariable
- [ ] Partial derivatives
- [ ] Gradient (∇f) — direction of steepest ascent
- [ ] Directional derivative
- [ ] Jacobian matrix
- [ ] Hessian matrix
- [ ] Chain rule (multivariable) — POWERS BACKPROP
- [ ] Multiple integrals
- [ ] Change of variables, Jacobian determinant

### Optimization
- [ ] Convex sets and convex functions
- [ ] First and second-order optimality conditions
- [ ] Unconstrained optimization
- [ ] Constrained optimization: Lagrange multipliers
- [ ] KKT conditions 🔵
- [ ] Gradient descent (and variants — see Deep Learning)

## 2.3 Probability 🔴

### Foundations
- [ ] Sample space, events, sigma-algebras 🔵
- [ ] Probability axioms (Kolmogorov)
- [ ] Combinatorics: permutations, combinations
- [ ] Conditional probability
- [ ] Independence (and conditional independence)
- [ ] Law of total probability
- [ ] Bayes' theorem (THE single most important formula in ML)

### Random Variables
- [ ] Discrete vs continuous random variables
- [ ] Probability Mass Function (PMF)
- [ ] Probability Density Function (PDF)
- [ ] Cumulative Distribution Function (CDF)
- [ ] Expectation E[X]
- [ ] Variance Var(X), standard deviation
- [ ] Moments, moment generating functions
- [ ] Covariance, correlation
- [ ] Independence vs uncorrelated (not the same!)

### Common Distributions
- [ ] Discrete: Bernoulli, Binomial, Geometric, Negative Binomial, Poisson, Categorical, Multinomial
- [ ] Continuous: Uniform, Normal (Gaussian), Exponential, Gamma, Beta, Chi-squared, Student's t, F-distribution, Dirichlet
- [ ] When each distribution is used

### Multivariate
- [ ] Joint, marginal, conditional distributions
- [ ] Multivariate Gaussian
- [ ] Covariance matrix
- [ ] Transformations of random variables

### Limit Theorems
- [ ] Law of large numbers (weak and strong)
- [ ] Central Limit Theorem (CLT)

### Stochastic Processes 🔵
- [ ] Markov chains
- [ ] Stationary distributions
- [ ] Hidden Markov Models (HMMs)
- [ ] Poisson processes

## 2.4 Statistics 🔴

- [ ] Descriptive statistics: mean, median, mode, percentiles, IQR
- [ ] Sampling: SRS, stratified, cluster, bias
- [ ] Estimators: bias, variance, MSE
- [ ] Maximum Likelihood Estimation (MLE)
- [ ] Maximum A Posteriori (MAP)
- [ ] Method of moments
- [ ] Confidence intervals
- [ ] Hypothesis testing: null/alternative hypotheses
- [ ] Type I and Type II errors, statistical power
- [ ] p-values (and what they don't mean)
- [ ] Common tests: z-test, t-test (one/two sample, paired), chi-squared, ANOVA, F-test
- [ ] Non-parametric tests: Mann-Whitney, Wilcoxon, Kruskal-Wallis
- [ ] Multiple testing corrections: Bonferroni, FDR (Benjamini-Hochberg)
- [ ] Bootstrap and permutation tests
- [ ] Bayesian statistics: prior, posterior, conjugacy
- [ ] MCMC basics 🔵
- [ ] Linear regression statistics: R², adjusted R², F-statistic
- [ ] A/B testing fundamentals
- [ ] Causal inference basics: confounding, RCTs, observational data, propensity scores 🟢

## 2.5 Discrete Mathematics 🟡

- [ ] Sets, functions, relations
- [ ] Logic: propositional, predicate
- [ ] Proof techniques: direct, contradiction, induction
- [ ] Combinatorics
- [ ] Graph theory: directed/undirected, weighted, trees, DAGs, paths, cycles
- [ ] Big-O, Big-Omega, Big-Theta notation
- [ ] Algorithm complexity (time and space)
- [ ] Recurrence relations
- [ ] Dynamic programming basics

## 2.6 Information Theory 🟡

- [ ] Entropy (Shannon)
- [ ] Joint entropy, conditional entropy
- [ ] Mutual information
- [ ] Cross-entropy
- [ ] KL divergence (Kullback-Leibler)
- [ ] JS divergence
- [ ] Coding theory basics: source coding, channel coding
- [ ] Perplexity (used in LM evaluation)

---

# Part 3: Data Engineering for ML

## 3.1 NumPy 🔴

- [ ] Array creation: `array`, `zeros`, `ones`, `empty`, `arange`, `linspace`, `eye`, `full`
- [ ] dtypes: int8/16/32/64, float16/32/64, bool, object
- [ ] Array attributes: `shape`, `ndim`, `size`, `dtype`, `itemsize`
- [ ] Indexing: basic, slicing, fancy (integer arrays), boolean masking
- [ ] Reshaping: `reshape`, `ravel`, `flatten`, `T` (transpose), `swapaxes`, `expand_dims`, `squeeze`, `newaxis`
- [ ] Concatenation: `concatenate`, `stack`, `vstack`, `hstack`, `dstack`, `column_stack`
- [ ] Splitting: `split`, `array_split`, `hsplit`, `vsplit`
- [ ] **Broadcasting** (deeply understand this — it makes fast code possible)
- [ ] Universal functions (ufuncs): vectorized operations
- [ ] Aggregation: `sum`, `mean`, `std`, `var`, `min`, `max`, `argmin`, `argmax`, `cumsum`, `cumprod`
- [ ] Axis parameter (when to use 0 vs 1 vs None)
- [ ] Linear algebra: `np.dot`, `np.matmul`, `@` operator, `np.linalg.inv`, `solve`, `eig`, `svd`, `norm`
- [ ] `np.einsum` (Einstein summation — power tool)
- [ ] Random module: `np.random.default_rng()`, `normal`, `uniform`, `choice`, `shuffle`, `permutation`
- [ ] Saving/loading: `np.save`, `np.load`, `np.savez`
- [ ] Memory layout: C-order vs F-order, views vs copies
- [ ] Performance: vectorization vs loops, masking vs filtering

## 3.2 Pandas 🔴

### Basics
- [ ] Series: creation, indexing, alignment
- [ ] DataFrame: creation from dicts, lists, NumPy arrays, files
- [ ] Reading data: `read_csv`, `read_excel`, `read_json`, `read_parquet`, `read_sql`, `read_html`
- [ ] Writing data: `to_csv`, `to_excel`, `to_parquet`, `to_sql`
- [ ] Index objects, multi-index, hierarchical indexing
- [ ] `dtypes` and conversion (`astype`)

### Selection & Indexing
- [ ] `.loc` (label-based) vs `.iloc` (integer-based)
- [ ] `.at`, `.iat` (single value access)
- [ ] Boolean masking
- [ ] `.query()` method
- [ ] `.isin()`, `.between()`
- [ ] Chained indexing pitfalls (SettingWithCopyWarning)

### Cleaning & Manipulation
- [ ] Missing data: `isna`, `notna`, `fillna`, `dropna`, `interpolate`
- [ ] Duplicates: `duplicated`, `drop_duplicates`
- [ ] Renaming: `rename` (columns and index)
- [ ] Dropping: `drop`, `drop_duplicates`
- [ ] Data types: `astype`, `to_datetime`, `to_numeric`
- [ ] String operations: `.str.*` accessor
- [ ] Categorical data: `pd.Categorical`, `.cat.*` accessor

### Aggregation & Grouping
- [ ] `groupby`: basics
- [ ] Aggregation functions: `agg`, `sum`, `mean`, `count`, `nunique`, custom
- [ ] Transformation: `transform`
- [ ] Filtration: `filter`
- [ ] Apply: `apply` (and when to avoid it)
- [ ] `value_counts`, `crosstab`, `pivot_table`

### Reshaping
- [ ] `pivot`, `pivot_table`
- [ ] `melt`
- [ ] `stack`, `unstack`
- [ ] `explode`
- [ ] `get_dummies` (one-hot encoding)

### Combining DataFrames
- [ ] `concat`
- [ ] `merge` (inner, left, right, outer, cross)
- [ ] `join`
- [ ] When to use which

### Time Series
- [ ] DatetimeIndex
- [ ] Resampling: `resample`, `asfreq`
- [ ] Rolling windows: `rolling`, `expanding`
- [ ] Shifting: `shift`, `diff`, `pct_change`
- [ ] Timezone handling

### Performance
- [ ] Vectorization over `apply`
- [ ] `eval` and `query` for large data
- [ ] Memory: `info(memory_usage='deep')`, downcasting dtypes
- [ ] When pandas isn't enough → Polars, Dask, Spark

## 3.3 Visualization 🟡

### Matplotlib
- [ ] Figure and Axes objects (pyplot vs OO interface)
- [ ] Plot types: line, scatter, bar, hist, boxplot, errorbar
- [ ] Subplots: `plt.subplots`, GridSpec
- [ ] Customization: titles, labels, legends, ticks, colors, styles
- [ ] Saving figures
- [ ] Animations

### Seaborn
- [ ] Distribution plots: `histplot`, `kdeplot`, `displot`
- [ ] Relational plots: `scatterplot`, `lineplot`, `relplot`
- [ ] Categorical plots: `boxplot`, `violinplot`, `swarmplot`, `barplot`, `catplot`
- [ ] Matrix plots: `heatmap`, `clustermap`
- [ ] `pairplot`, `jointplot`
- [ ] Themes and styling

### Interactive
- [ ] Plotly: `plotly.express`, `plotly.graph_objects`
- [ ] Bokeh basics 🟢
- [ ] Altair (declarative grammar of graphics) 🟢
- [ ] Streamlit / Gradio for dashboards
- [ ] Dash for complex dashboards 🟢

## 3.4 SQL 🔴

- [ ] SELECT, FROM, WHERE
- [ ] ORDER BY, LIMIT, OFFSET
- [ ] DISTINCT
- [ ] Aggregation: COUNT, SUM, AVG, MIN, MAX
- [ ] GROUP BY, HAVING
- [ ] JOINs: INNER, LEFT, RIGHT, FULL OUTER, CROSS, SELF
- [ ] UNION, UNION ALL, INTERSECT, EXCEPT
- [ ] Subqueries (correlated and uncorrelated)
- [ ] CTEs (`WITH` clauses)
- [ ] Window functions: `ROW_NUMBER`, `RANK`, `DENSE_RANK`, `NTILE`, `LAG`, `LEAD`, `SUM() OVER`, `PARTITION BY`
- [ ] CASE WHEN
- [ ] String functions: SUBSTR, CONCAT, REPLACE, TRIM, UPPER/LOWER
- [ ] Date functions
- [ ] NULL handling: IS NULL, COALESCE, NULLIF
- [ ] DDL: CREATE, ALTER, DROP, TRUNCATE
- [ ] DML: INSERT, UPDATE, DELETE, UPSERT
- [ ] Transactions: BEGIN, COMMIT, ROLLBACK, ACID
- [ ] Indexes: B-tree, hash, when to add
- [ ] Query plans, EXPLAIN

## 3.5 Databases 🟡

- [ ] Relational: PostgreSQL (preferred), MySQL, SQLite
- [ ] NoSQL document: MongoDB
- [ ] Key-value: Redis (caching, queues)
- [ ] Wide-column: Cassandra 🟢
- [ ] Time-series: TimescaleDB, InfluxDB 🟢
- [ ] Graph: Neo4j 🟢
- [ ] Vector databases: pgvector, Pinecone, Weaviate, Qdrant, Chroma, Milvus, LanceDB
- [ ] ORMs: SQLAlchemy (Python), SQLModel
- [ ] Database connections: psycopg2, pymongo

## 3.6 Big Data & Distributed 🟢

- [ ] Apache Spark / PySpark: RDDs, DataFrames, Spark SQL
- [ ] Dask (NumPy/Pandas API on bigger data)
- [ ] Polars (modern, fast pandas alternative — learn this)
- [ ] Ray (distributed compute)
- [ ] Apache Arrow (memory format)
- [ ] Parquet, ORC file formats
- [ ] Delta Lake, Apache Iceberg, Apache Hudi (lakehouse)
- [ ] Kafka basics (streaming) 🟢

## 3.7 Data Acquisition 🟡

- [ ] Web scraping: `requests` + `BeautifulSoup`
- [ ] `Scrapy` framework
- [ ] Browser automation: `Playwright`, `Selenium`
- [ ] APIs: REST, GraphQL, rate limiting, auth (OAuth, API keys)
- [ ] Data sources: Kaggle, UCI ML, Hugging Face Datasets, OpenML, government open data
- [ ] Synthetic data generation: Faker, SDV
- [ ] Data labeling: Label Studio, Prodigy, Roboflow

---

# Part 4: Classical Machine Learning

## 4.1 Core Concepts 🔴

- [ ] Supervised vs unsupervised vs semi-supervised vs self-supervised vs reinforcement
- [ ] Regression vs classification vs ranking
- [ ] Train / validation / test splits
- [ ] Cross-validation: k-fold, stratified, leave-one-out, time series (TimeSeriesSplit), nested CV
- [ ] Bias-variance tradeoff
- [ ] Overfitting and underfitting
- [ ] Generalization, train/test gap
- [ ] Curse of dimensionality
- [ ] No free lunch theorem
- [ ] Data leakage (train-test contamination) — common pitfall
- [ ] Label leakage

## 4.2 Supervised Learning Algorithms 🔴

### Linear Models
- [ ] Linear regression (OLS, gradient descent)
- [ ] Polynomial regression
- [ ] Ridge regression (L2 regularization)
- [ ] Lasso regression (L1 regularization)
- [ ] Elastic Net
- [ ] Logistic regression (binary, multinomial)
- [ ] Softmax regression
- [ ] Generalized Linear Models (GLMs)
- [ ] Bayesian linear regression 🔵

### Instance-Based
- [ ] K-Nearest Neighbors (KNN) — classification and regression
- [ ] Distance metrics: Euclidean, Manhattan, Minkowski, cosine, Mahalanobis
- [ ] KD-trees, Ball trees (for fast KNN)

### Probabilistic
- [ ] Naive Bayes: Gaussian, Multinomial, Bernoulli, Complement
- [ ] Linear Discriminant Analysis (LDA)
- [ ] Quadratic Discriminant Analysis (QDA)

### Tree-Based
- [ ] Decision trees: CART, ID3, C4.5
- [ ] Splitting criteria: Gini impurity, entropy, MSE
- [ ] Pruning: pre-pruning, post-pruning
- [ ] Random Forests
- [ ] Extra Trees (Extremely Randomized Trees)

### Boosting (often wins Kaggle)
- [ ] AdaBoost
- [ ] Gradient Boosting Machines (GBM)
- [ ] XGBoost (master this)
- [ ] LightGBM
- [ ] CatBoost
- [ ] HistGradientBoosting (scikit-learn)

### Support Vector Machines
- [ ] Linear SVM, margin maximization
- [ ] Soft margin, C hyperparameter
- [ ] Kernel trick
- [ ] Kernels: linear, polynomial, RBF (Gaussian), sigmoid
- [ ] SVR (Support Vector Regression)

### Other
- [ ] Perceptron (historical, links to neural nets)
- [ ] Passive Aggressive
- [ ] Stochastic Gradient Descent classifier/regressor

## 4.3 Unsupervised Learning 🔴

### Clustering
- [ ] K-Means (and K-Means++)
- [ ] Mini-batch K-Means
- [ ] Hierarchical clustering (agglomerative, divisive)
- [ ] Linkage: single, complete, average, Ward
- [ ] DBSCAN, HDBSCAN
- [ ] OPTICS
- [ ] Mean Shift
- [ ] Spectral clustering
- [ ] Gaussian Mixture Models (GMM) — EM algorithm
- [ ] Affinity Propagation
- [ ] BIRCH

### Association
- [ ] Apriori algorithm 🟢
- [ ] FP-Growth 🟢
- [ ] Market basket analysis

## 4.4 Dimensionality Reduction 🟡

- [ ] PCA (Principal Component Analysis)
- [ ] Kernel PCA
- [ ] Sparse PCA
- [ ] Incremental PCA
- [ ] Truncated SVD
- [ ] LDA (Linear Discriminant Analysis) — supervised
- [ ] ICA (Independent Component Analysis)
- [ ] Factor Analysis
- [ ] NMF (Non-negative Matrix Factorization)
- [ ] t-SNE — for visualization
- [ ] UMAP — for visualization (and sometimes input)
- [ ] Autoencoders (deep learning approach)

## 4.5 Anomaly Detection 🟢

- [ ] Statistical: z-score, IQR
- [ ] Isolation Forest
- [ ] One-Class SVM
- [ ] Local Outlier Factor (LOF)
- [ ] DBSCAN for anomaly detection
- [ ] Autoencoder-based 🟢
- [ ] Time series anomaly detection 🟢

## 4.6 Feature Engineering 🔴

### Scaling
- [ ] StandardScaler (z-score)
- [ ] MinMaxScaler
- [ ] RobustScaler
- [ ] MaxAbsScaler
- [ ] Normalizer (per-row)
- [ ] PowerTransformer (Box-Cox, Yeo-Johnson)
- [ ] QuantileTransformer

### Encoding Categoricals
- [ ] One-hot encoding
- [ ] Label encoding
- [ ] Ordinal encoding
- [ ] Target encoding (mean encoding) — leakage caution
- [ ] Frequency encoding
- [ ] Hash encoding
- [ ] Binary encoding
- [ ] Weight of Evidence (WoE)
- [ ] Embeddings for high-cardinality

### Feature Creation
- [ ] Polynomial features
- [ ] Interaction features
- [ ] Binning / discretization
- [ ] Date/time features (day of week, month, holiday, etc.)
- [ ] Aggregations (group statistics)
- [ ] Domain-specific features

### Feature Selection
- [ ] Filter methods: variance threshold, chi-squared, mutual information, ANOVA F-test
- [ ] Wrapper methods: forward selection, backward elimination, RFE (Recursive Feature Elimination)
- [ ] Embedded methods: L1 regularization, tree-based importance
- [ ] Permutation importance
- [ ] SHAP-based selection

## 4.7 Model Evaluation 🔴

### Regression Metrics
- [ ] MAE (Mean Absolute Error)
- [ ] MSE (Mean Squared Error)
- [ ] RMSE
- [ ] R² (coefficient of determination)
- [ ] Adjusted R²
- [ ] MAPE (Mean Absolute Percentage Error) — pitfalls
- [ ] MSLE (Mean Squared Log Error)
- [ ] Huber loss
- [ ] Quantile loss

### Classification Metrics
- [ ] Accuracy (and why it can be misleading)
- [ ] Confusion matrix
- [ ] Precision, Recall, F1, F-beta
- [ ] Macro vs micro vs weighted averaging
- [ ] ROC curve, AUC
- [ ] Precision-Recall curve, Average Precision
- [ ] Log loss / cross-entropy
- [ ] Cohen's kappa
- [ ] Matthews Correlation Coefficient (MCC)
- [ ] Top-K accuracy
- [ ] Multi-label metrics: Hamming loss, Jaccard

### Clustering Metrics
- [ ] Silhouette score
- [ ] Davies-Bouldin index
- [ ] Calinski-Harabasz index
- [ ] Adjusted Rand Index (ARI)
- [ ] Normalized Mutual Information (NMI)

### Ranking Metrics 🟢
- [ ] NDCG
- [ ] MAP (Mean Average Precision)
- [ ] MRR (Mean Reciprocal Rank)

### Calibration 🟡
- [ ] Calibration curves (reliability diagrams)
- [ ] Brier score
- [ ] Platt scaling, isotonic regression

## 4.8 Ensembles 🟡

- [ ] Bagging
- [ ] Boosting (see boosting algorithms above)
- [ ] Stacking
- [ ] Blending
- [ ] Voting (hard and soft)

## 4.9 Imbalanced Data 🟡

- [ ] Class weights
- [ ] Resampling: random over/undersampling
- [ ] SMOTE, ADASYN
- [ ] Tomek links, ENN (cleaning)
- [ ] Threshold tuning
- [ ] Cost-sensitive learning
- [ ] Focal loss
- [ ] `imbalanced-learn` library

## 4.10 Hyperparameter Optimization 🔴

- [ ] Grid search (`GridSearchCV`)
- [ ] Random search (`RandomizedSearchCV`)
- [ ] Bayesian optimization
- [ ] Optuna (best library)
- [ ] Hyperopt
- [ ] Ray Tune
- [ ] Successive halving, Hyperband
- [ ] Population-based training 🔵

## 4.11 scikit-learn 🔴

- [ ] Estimator API: fit, predict, transform
- [ ] Pipelines (`Pipeline`, `make_pipeline`)
- [ ] ColumnTransformer for heterogeneous features
- [ ] FeatureUnion
- [ ] Custom transformers (inherit BaseEstimator, TransformerMixin)
- [ ] Persistence: `joblib.dump`/`load`
- [ ] Model selection helpers: `train_test_split`, `cross_val_score`, `cross_validate`
- [ ] Preprocessing module
- [ ] Metrics module
- [ ] Calibration tools

---

# Part 5: Deep Learning

## 5.1 Fundamentals 🔴

- [ ] Perceptron, history of neural networks
- [ ] Multilayer perceptron (MLP)
- [ ] Universal approximation theorem
- [ ] Forward propagation
- [ ] Backpropagation (derive it once by hand)
- [ ] Computational graphs, automatic differentiation
- [ ] Tensors (n-dimensional arrays)

## 5.2 Activation Functions 🔴

- [ ] Sigmoid (and vanishing gradient problem)
- [ ] Tanh
- [ ] ReLU (and dying ReLU)
- [ ] Leaky ReLU, Parametric ReLU
- [ ] ELU, SELU
- [ ] GELU (used in transformers)
- [ ] SiLU / Swish
- [ ] Softmax (output layer for classification)
- [ ] Mish

## 5.3 Loss Functions 🔴

- [ ] Regression: MSE, MAE, Huber, Log-cosh, Quantile
- [ ] Binary classification: BCE (Binary Cross-Entropy)
- [ ] Multi-class: Categorical CE, Sparse Categorical CE
- [ ] Focal loss (imbalanced classification)
- [ ] Hinge loss (SVM)
- [ ] Triplet loss, Contrastive loss (metric learning, embeddings)
- [ ] KL divergence loss (distribution matching)
- [ ] CTC loss (sequence alignment)
- [ ] Dice loss, IoU loss (segmentation)

## 5.4 Optimizers 🔴

- [ ] SGD (Stochastic Gradient Descent)
- [ ] SGD with momentum
- [ ] Nesterov accelerated gradient
- [ ] AdaGrad
- [ ] RMSprop
- [ ] Adam (most common default)
- [ ] AdamW (Adam with decoupled weight decay)
- [ ] Adafactor (memory-efficient, for large models)
- [ ] LAMB
- [ ] Lion
- [ ] Sophia
- [ ] Shampoo, K-FAC 🔵

## 5.5 Learning Rate Schedules 🔴

- [ ] Constant
- [ ] Step decay
- [ ] Exponential decay
- [ ] Cosine annealing
- [ ] Cosine with warm restarts
- [ ] Linear warmup + cosine decay (transformer standard)
- [ ] One-Cycle policy
- [ ] Reduce on plateau

## 5.6 Weight Initialization 🟡

- [ ] Why initialization matters
- [ ] Xavier / Glorot (sigmoid, tanh)
- [ ] He / Kaiming (ReLU)
- [ ] Orthogonal
- [ ] Pretrained weights

## 5.7 Regularization 🔴

- [ ] L1, L2 weight decay
- [ ] Dropout (and variants: Spatial, DropConnect, DropPath)
- [ ] Batch Normalization
- [ ] Layer Normalization (used in transformers)
- [ ] Group Normalization
- [ ] Instance Normalization
- [ ] RMSNorm (used in LLaMA)
- [ ] Early stopping
- [ ] Data augmentation (regularizer by another name)
- [ ] Label smoothing
- [ ] Mixup, CutMix, CutOut
- [ ] Stochastic depth

## 5.8 Training Stability 🟡

- [ ] Gradient clipping (norm-based, value-based)
- [ ] Mixed precision: fp16, bf16, fp8
- [ ] Loss scaling (for fp16)
- [ ] Numerical stability tricks

## 5.9 CNN Architectures 🟡

- [ ] Convolution operation: kernels, stride, padding, dilation
- [ ] Pooling: max, average, global average
- [ ] Receptive field
- [ ] LeNet-5
- [ ] AlexNet
- [ ] VGG
- [ ] Inception / GoogLeNet (1x1 convs, inception modules)
- [ ] ResNet (skip/residual connections — game-changer)
- [ ] ResNeXt
- [ ] DenseNet
- [ ] MobileNet (depthwise separable convs)
- [ ] EfficientNet (compound scaling)
- [ ] ConvNeXt (modernized CNN)
- [ ] Vision Transformer alternatives in CNN space

## 5.10 RNN / Sequence Models 🟢 (mostly historical now, but understand)

- [ ] Vanilla RNN
- [ ] BPTT (Backpropagation Through Time)
- [ ] Vanishing/exploding gradients in RNNs
- [ ] LSTM (cell state, forget/input/output gates)
- [ ] GRU
- [ ] Bidirectional RNNs
- [ ] Stacked RNNs
- [ ] Seq2seq with attention (Bahdanau, Luong)
- [ ] Teacher forcing
- [ ] Beam search decoding

## 5.11 Transformers 🔴 (the architecture that runs the world)

- [ ] Self-attention (Q, K, V) — derive from scratch
- [ ] Scaled dot-product attention
- [ ] Multi-head attention
- [ ] Positional encoding: sinusoidal, learned, RoPE (Rotary), ALiBi, NoPE
- [ ] Feed-forward block (MLP)
- [ ] Residual connections in transformers
- [ ] Layer norm: pre-norm vs post-norm
- [ ] Encoder block, decoder block
- [ ] Encoder-only: BERT-style
- [ ] Decoder-only: GPT-style (with causal masking)
- [ ] Encoder-decoder: T5-style
- [ ] Causal / autoregressive masking
- [ ] Cross-attention
- [ ] KV cache (inference optimization)
- [ ] Flash Attention v1/v2/v3
- [ ] Multi-Query Attention (MQA)
- [ ] Grouped-Query Attention (GQA)
- [ ] Sliding Window Attention
- [ ] Sparse attention patterns
- [ ] Linear attention 🔵
- [ ] State Space Models: Mamba, S4, S6 🔵

## 5.12 Generative Models 🟢

### Autoencoders
- [ ] Vanilla autoencoder
- [ ] Denoising autoencoder
- [ ] Sparse autoencoder
- [ ] Variational Autoencoder (VAE) — reparameterization trick, ELBO
- [ ] β-VAE, VQ-VAE

### GANs
- [ ] GAN basics: generator, discriminator, minimax game
- [ ] Mode collapse
- [ ] DCGAN
- [ ] WGAN, WGAN-GP (Wasserstein)
- [ ] StyleGAN, StyleGAN2/3
- [ ] CycleGAN
- [ ] Pix2Pix
- [ ] BigGAN

### Diffusion Models 🔴 (current SOTA for images)
- [ ] DDPM (Denoising Diffusion Probabilistic Models)
- [ ] DDIM (faster sampling)
- [ ] Score-based models
- [ ] Latent Diffusion (Stable Diffusion)
- [ ] Classifier-free guidance
- [ ] ControlNet
- [ ] LoRA for diffusion
- [ ] DreamBooth, Textual Inversion
- [ ] Consistency models, distillation

### Other Generative
- [ ] Normalizing flows 🔵
- [ ] Energy-based models 🔵
- [ ] Autoregressive image models (PixelCNN, etc.)

## 5.13 Frameworks 🔴

### PyTorch (primary)
- [ ] Tensors: creation, ops, GPU
- [ ] Autograd: `requires_grad`, `backward`, `grad`
- [ ] `nn.Module`: custom layers, models
- [ ] `nn` building blocks
- [ ] DataLoader, Dataset, Sampler
- [ ] Training loop pattern
- [ ] Optimizers and schedulers
- [ ] Saving/loading models (`state_dict`)
- [ ] torch.compile (PyTorch 2.0+)
- [ ] CUDA, device management
- [ ] Distributed: DDP, FSDP
- [ ] Mixed precision: `torch.cuda.amp`, `torch.amp`
- [ ] TorchScript 🟢
- [ ] ONNX export

### PyTorch Ecosystem
- [ ] PyTorch Lightning (boilerplate reduction)
- [ ] Hugging Face Accelerate
- [ ] timm (vision models)
- [ ] torchvision, torchaudio, torchtext

### TensorFlow / Keras 🟢
- [ ] Sequential, Functional, Subclassing APIs
- [ ] `tf.data` pipelines
- [ ] Eager vs graph mode
- [ ] TF Hub
- [ ] When you'll encounter it (lots of legacy code)

### JAX 🟢🔵
- [ ] Functional programming style
- [ ] `jit`, `vmap`, `grad`, `pmap`
- [ ] Flax, Haiku (NN libraries on JAX)
- [ ] Used heavily at Google/DeepMind

---

# Part 6: NLP & Large Language Models

## 6.1 Classical NLP Foundations 🟡

- [ ] Text preprocessing pipelines
- [ ] Tokenization: whitespace, word, character
- [ ] Stemming (Porter, Snowball), Lemmatization
- [ ] Stop words, punctuation handling
- [ ] N-grams (uni, bi, tri)
- [ ] POS (Part of Speech) tagging
- [ ] Named Entity Recognition (NER)
- [ ] Dependency parsing, constituency parsing 🟢
- [ ] Bag of Words (BoW)
- [ ] TF-IDF
- [ ] Topic modeling: LDA (Latent Dirichlet Allocation), NMF
- [ ] Sentiment analysis (classical)
- [ ] `NLTK`, `spaCy`

## 6.2 Modern Tokenization 🔴

- [ ] Subword tokenization (why subwords)
- [ ] BPE (Byte-Pair Encoding) — used by GPT
- [ ] WordPiece — used by BERT
- [ ] SentencePiece
- [ ] Unigram language model tokenization
- [ ] Tiktoken (OpenAI)
- [ ] Vocabulary size tradeoffs
- [ ] Special tokens (BOS, EOS, PAD, UNK, system tokens)

## 6.3 Word Embeddings 🟡

- [ ] Distributional hypothesis
- [ ] Word2Vec: CBOW, Skip-gram
- [ ] Negative sampling, hierarchical softmax
- [ ] GloVe
- [ ] FastText (subword embeddings)
- [ ] ELMo (contextualized) 🟢
- [ ] Sentence embeddings: Sentence-BERT, SimCSE
- [ ] Modern embedding models: text-embedding-3, BGE, E5, Voyage, Cohere embed

## 6.4 LLM Architecture & Models 🔴

### Encoder Models
- [ ] BERT (pretraining: MLM + NSP)
- [ ] RoBERTa
- [ ] DistilBERT
- [ ] ALBERT
- [ ] DeBERTa, DeBERTa-v3
- [ ] ELECTRA (replaced token detection)
- [ ] XLM, XLM-R (multilingual)

### Decoder Models
- [ ] GPT series (GPT-1, 2, 3, 3.5, 4, 4o, etc.)
- [ ] LLaMA family (1, 2, 3, 3.1, 3.2, 3.3)
- [ ] Mistral 7B, Mixtral 8x7B (MoE)
- [ ] Qwen family
- [ ] Gemma 2 / 3
- [ ] Phi family (small models)
- [ ] Falcon
- [ ] DeepSeek (V2, V3, R1)
- [ ] Yi
- [ ] Command-R, Command-R+ (Cohere)
- [ ] Claude (Anthropic)
- [ ] Open vs closed weights distinction

### Encoder-Decoder
- [ ] T5, FLAN-T5
- [ ] BART
- [ ] mT5, mBART (multilingual)
- [ ] UL2

## 6.5 Training LLMs (conceptual) 🟡

### Pretraining
- [ ] Next-token prediction objective
- [ ] Data curation, deduplication
- [ ] Scaling laws (Chinchilla, etc.)
- [ ] Compute-optimal training

### Post-training / Alignment
- [ ] Supervised Fine-Tuning (SFT)
- [ ] Instruction tuning
- [ ] RLHF: reward model, PPO
- [ ] DPO (Direct Preference Optimization)
- [ ] ORPO, KTO, GRPO, SimPO (newer methods)
- [ ] Constitutional AI 🟢
- [ ] RLAIF
- [ ] Iterative refinement / online DPO

### Architectural Variants
- [ ] Mixture of Experts (MoE)
- [ ] Mixture of Depths
- [ ] Sparse models

## 6.6 Fine-Tuning 🔴

- [ ] Full fine-tuning (when feasible)
- [ ] Parameter-Efficient Fine-Tuning (PEFT)
- [ ] LoRA (Low-Rank Adaptation)
- [ ] QLoRA (quantized LoRA)
- [ ] DoRA
- [ ] Adapters
- [ ] Prefix tuning
- [ ] Prompt tuning
- [ ] IA³
- [ ] Hugging Face `peft` library
- [ ] `trl` library (SFT, DPO trainers)
- [ ] Unsloth (fast fine-tuning)
- [ ] Axolotl
- [ ] Catastrophic forgetting

## 6.7 Prompt Engineering 🔴

- [ ] Zero-shot, few-shot prompting
- [ ] In-context learning
- [ ] Chain of Thought (CoT)
- [ ] Self-consistency
- [ ] Tree of Thoughts, Graph of Thoughts
- [ ] ReAct (Reasoning + Acting)
- [ ] Reflexion
- [ ] System prompts, role prompts
- [ ] Output formatting, JSON mode
- [ ] Structured outputs (Instructor, Outlines, Pydantic AI)
- [ ] Function calling / tool use
- [ ] Prompt injection awareness (defensive)
- [ ] Prompt versioning & testing

## 6.8 Agents 🟡 (hot area)

- [ ] What is an agent (LLM + tools + memory + planning)
- [ ] Tool use / function calling
- [ ] ReAct pattern
- [ ] Planning: task decomposition
- [ ] Memory: short-term, long-term, episodic
- [ ] Multi-agent systems
- [ ] Agent frameworks: LangGraph, CrewAI, AutoGen, Smolagents
- [ ] Evaluating agents (especially hard)
- [ ] Sandboxing and safety

## 6.9 Retrieval-Augmented Generation (RAG) 🔴

### Embeddings
- [ ] Choosing embedding models
- [ ] Embedding dimension tradeoffs
- [ ] Domain-specific embeddings

### Chunking
- [ ] Fixed-size chunking
- [ ] Recursive / sentence-aware chunking
- [ ] Semantic chunking
- [ ] Late chunking
- [ ] Chunk overlap

### Retrieval
- [ ] Vector search (cosine, dot product, Euclidean)
- [ ] Sparse retrieval: BM25, TF-IDF
- [ ] Hybrid search (sparse + dense)
- [ ] Re-ranking: cross-encoders, Cohere rerank
- [ ] HyDE (Hypothetical Document Embeddings)
- [ ] Query expansion, query rewriting
- [ ] Multi-query, sub-query decomposition
- [ ] ColBERT (multi-vector retrieval)
- [ ] GraphRAG
- [ ] Agentic RAG
- [ ] Self-querying retrievers

### Vector Databases
- [ ] pgvector (PostgreSQL)
- [ ] Chroma
- [ ] Qdrant
- [ ] Weaviate
- [ ] Pinecone (managed)
- [ ] Milvus
- [ ] LanceDB
- [ ] FAISS (library, not DB)
- [ ] HNSW, IVF, PQ (indexing algorithms)

## 6.10 LLM Inference & Production 🟡

- [ ] Inference servers: vLLM, TGI (Text Generation Inference), SGLang, TensorRT-LLM, llama.cpp, MLC LLM
- [ ] Batching: static, dynamic, continuous (in-flight)
- [ ] PagedAttention (vLLM's contribution)
- [ ] Speculative decoding
- [ ] Streaming responses
- [ ] Token caching, prefix caching
- [ ] Semantic caching
- [ ] Quantization: GPTQ, AWQ, GGUF (llama.cpp), bitsandbytes, FP8
- [ ] Quantization-aware training (QAT)
- [ ] Knowledge distillation
- [ ] Pruning: structured, unstructured
- [ ] Hosting: Replicate, RunPod, Together AI, Anyscale, Modal, Lambda Labs, Fireworks

## 6.11 LLM Evaluation 🟡

- [ ] Classical metrics: BLEU, ROUGE, METEOR, BERTScore, BLEURT
- [ ] Perplexity
- [ ] Benchmarks: MMLU, MMLU-Pro, GSM8K, MATH, HumanEval, MBPP, BIG-Bench, HellaSwag, ARC, TruthfulQA, GPQA
- [ ] Chat benchmarks: MT-Bench, AlpacaEval, Arena ELO
- [ ] LLM-as-judge (and its biases)
- [ ] RAG evaluation: RAGAS (faithfulness, answer relevancy, context precision/recall), TruLens
- [ ] Hallucination detection
- [ ] Red teaming, adversarial testing
- [ ] Bias evaluation
- [ ] Tools: lm-evaluation-harness, OpenCompass, DeepEval

## 6.12 Frameworks (LLM apps) 🟡

- [ ] LangChain, LangGraph (popular but opinionated)
- [ ] LlamaIndex (RAG-focused)
- [ ] DSPy (compile prompts)
- [ ] Haystack
- [ ] Semantic Kernel (Microsoft)
- [ ] Pydantic AI
- [ ] Instructor (structured outputs)
- [ ] Outlines (constrained generation)
- [ ] Guidance
- [ ] Hugging Face `transformers`, `datasets`, `tokenizers`, `peft`, `trl`, `accelerate`

---

# Part 7: Computer Vision

## 7.1 Image Fundamentals 🟡

- [ ] Image representation: pixels, channels
- [ ] Color spaces: RGB, BGR (OpenCV default!), HSV, LAB, YCbCr, Grayscale
- [ ] Image formats: JPEG, PNG, WebP, TIFF
- [ ] Resolution, aspect ratio, DPI
- [ ] Reading/writing images: PIL, OpenCV, imageio

## 7.2 Image Preprocessing 🟡

- [ ] Resizing (interpolation methods)
- [ ] Cropping (random, center)
- [ ] Padding
- [ ] Normalization (per channel)
- [ ] Color jitter, brightness, contrast, saturation, hue
- [ ] Augmentation libraries: `torchvision.transforms` (v2), `Albumentations`, `Kornia`

## 7.3 Classical CV 🟢

- [ ] Filtering: Gaussian, median, bilateral
- [ ] Edge detection: Sobel, Laplacian, Canny
- [ ] Corner detection: Harris, Shi-Tomasi
- [ ] Feature descriptors: SIFT, SURF, ORB, BRIEF
- [ ] Image matching, homography, RANSAC
- [ ] Morphological operations: erosion, dilation, opening, closing
- [ ] Histogram operations: equalization, CLAHE
- [ ] Hough transform (lines, circles)
- [ ] Watershed segmentation
- [ ] OpenCV library

## 7.4 Vision Architectures 🔴

- [ ] CNN backbones (see Part 5.9)
- [ ] Vision Transformer (ViT)
- [ ] DeiT (data-efficient ViT)
- [ ] Swin Transformer (hierarchical)
- [ ] MaxViT, CoAtNet (hybrid)
- [ ] timm library (model zoo)
- [ ] Transfer learning, fine-tuning vision models

## 7.5 Object Detection 🟢

- [ ] Concepts: bounding boxes, IoU, NMS, anchor boxes
- [ ] Two-stage: R-CNN, Fast R-CNN, Faster R-CNN, Mask R-CNN
- [ ] One-stage: YOLO (v3, v4, v5, v8, v10, v11), SSD, RetinaNet
- [ ] DETR (Detection Transformer), Deformable DETR, RT-DETR
- [ ] Anchor-free: FCOS, CenterNet
- [ ] Datasets: COCO, Pascal VOC, Open Images
- [ ] Metrics: mAP, mAP@IoU thresholds, mAP@small/medium/large

## 7.6 Segmentation 🟢

- [ ] Semantic segmentation
- [ ] Instance segmentation
- [ ] Panoptic segmentation
- [ ] U-Net (medical imaging classic)
- [ ] FCN
- [ ] DeepLab v1/v2/v3/v3+
- [ ] Mask R-CNN
- [ ] SAM, SAM 2 (Segment Anything — foundation model)
- [ ] Metrics: IoU, Dice, pixel accuracy

## 7.7 Generative Vision 🟢

- [ ] GANs (see Part 5.12)
- [ ] Stable Diffusion (master this if interested in this area)
- [ ] ControlNet, T2I-Adapter
- [ ] LoRA for diffusion
- [ ] DreamBooth, Textual Inversion
- [ ] Inpainting, outpainting
- [ ] Image-to-image, depth conditioning
- [ ] FLUX, SD3 (newer models)
- [ ] Video generation: Sora, Veo, Kling, etc.

## 7.8 Multimodal & Vision-Language 🟡

- [ ] CLIP (contrastive language-image pretraining)
- [ ] SigLIP
- [ ] BLIP, BLIP-2
- [ ] LLaVA, LLaVA-NeXT (open VLMs)
- [ ] Flamingo, GPT-4V architecture (conceptual)
- [ ] Qwen-VL, InternVL
- [ ] Vision-language tasks: VQA, captioning, retrieval

## 7.9 3D Vision 🔵

- [ ] Depth estimation: MiDaS, Depth Anything
- [ ] Point clouds: PointNet, PointNet++
- [ ] NeRF (Neural Radiance Fields)
- [ ] 3D Gaussian Splatting (current SOTA)
- [ ] SfM (Structure from Motion)

## 7.10 Video 🟢

- [ ] Optical flow: Lucas-Kanade, Farneback, RAFT
- [ ] Action recognition: I3D, SlowFast, TimeSformer, VideoMAE
- [ ] Object tracking: SORT, DeepSORT, ByteTrack
- [ ] Video segmentation
- [ ] Temporal models

---

# Part 8: Reinforcement Learning 🟢

## 8.1 Foundations

- [ ] Agent, environment, state, action, reward
- [ ] Markov Decision Processes (MDPs)
- [ ] Policy, value function, Q-function
- [ ] Bellman equations
- [ ] Exploration vs exploitation
- [ ] On-policy vs off-policy
- [ ] Model-based vs model-free

## 8.2 Classical RL

- [ ] Dynamic Programming: value iteration, policy iteration
- [ ] Monte Carlo methods
- [ ] Temporal Difference (TD) learning
- [ ] SARSA
- [ ] Q-Learning

## 8.3 Deep RL

- [ ] DQN (Deep Q-Network)
- [ ] Double DQN
- [ ] Dueling DQN
- [ ] Prioritized Experience Replay
- [ ] Rainbow DQN
- [ ] Policy Gradient theorem
- [ ] REINFORCE
- [ ] Actor-Critic (A2C, A3C)
- [ ] TRPO
- [ ] PPO (most-used policy method)
- [ ] DDPG, TD3 (continuous control)
- [ ] SAC (Soft Actor-Critic)

## 8.4 Advanced 🔵

- [ ] Model-based RL: Dreamer, MuZero
- [ ] Multi-agent RL
- [ ] Inverse RL
- [ ] Offline RL
- [ ] Hierarchical RL
- [ ] Meta-RL

## 8.5 RL for LLMs (critically important now) 🔴

- [ ] RLHF pipeline
- [ ] Reward model training
- [ ] PPO for language models
- [ ] DPO and successors
- [ ] Process reward models
- [ ] Reasoning RL (DeepSeek R1 style)

## 8.6 Tools

- [ ] Gymnasium (formerly Gym)
- [ ] Stable-Baselines3
- [ ] Ray RLlib
- [ ] CleanRL (educational)
- [ ] TRL (Hugging Face)

---

# Part 9: MLOps & Production

## 9.1 Software Engineering Practices 🔴

- [ ] Project structure (cookiecutter-data-science, hydra)
- [ ] Configuration management: Hydra, OmegaConf, Pydantic Settings, environment variables
- [ ] Logging (structured: loguru, structlog)
- [ ] Code quality (linters, formatters, type checkers)
- [ ] Testing ML code: unit, integration, data tests
- [ ] Documentation: docstrings, Sphinx, MkDocs

## 9.2 Containerization 🔴

- [ ] Docker fundamentals
- [ ] Dockerfile best practices
- [ ] Multi-stage builds
- [ ] Layer caching
- [ ] docker-compose
- [ ] Docker volumes, networks
- [ ] Image registries (Docker Hub, ECR, GCR, GAR)
- [ ] Container security basics

## 9.3 Orchestration 🟡

- [ ] Kubernetes concepts: pods, deployments, services, ingress, configmaps, secrets
- [ ] Jobs, CronJobs (batch workloads)
- [ ] Resource requests/limits
- [ ] Helm charts
- [ ] kubectl basics
- [ ] Managed K8s: EKS, GKE, AKS

## 9.4 Cloud Platforms 🟡 (pick one to go deep)

### AWS
- [ ] IAM (auth basics)
- [ ] S3 (storage)
- [ ] EC2 (compute)
- [ ] Lambda (serverless)
- [ ] ECR, ECS, EKS
- [ ] SageMaker (training, inference, pipelines)
- [ ] Bedrock (LLM access)
- [ ] Step Functions
- [ ] CloudWatch

### GCP
- [ ] IAM
- [ ] Cloud Storage
- [ ] Compute Engine
- [ ] Cloud Functions, Cloud Run
- [ ] Vertex AI (training, deployment, pipelines)
- [ ] GKE
- [ ] BigQuery (data warehouse)

### Azure
- [ ] Azure ML
- [ ] AKS
- [ ] Azure OpenAI Service

## 9.5 Model Serving 🔴

- [ ] REST APIs with FastAPI (canonical)
- [ ] Flask (older)
- [ ] gRPC
- [ ] TorchServe
- [ ] TF Serving
- [ ] NVIDIA Triton Inference Server (production scale)
- [ ] BentoML
- [ ] Ray Serve
- [ ] Seldon Core
- [ ] KServe
- [ ] vLLM (LLM serving)
- [ ] Modal, Replicate, Banana (serverless GPU)

## 9.6 Experiment Tracking & Model Registry 🔴

- [ ] MLflow (tracking + registry, open source)
- [ ] Weights & Biases (W&B) — popular, polished
- [ ] Neptune
- [ ] Comet ML
- [ ] ClearML
- [ ] TensorBoard
- [ ] DVC (data version control)
- [ ] Hugging Face Hub as registry

## 9.7 Pipelines & Orchestration 🟡

- [ ] Apache Airflow (canonical)
- [ ] Prefect (modern alternative)
- [ ] Dagster (asset-based)
- [ ] Kubeflow Pipelines
- [ ] Metaflow (Netflix's tool)
- [ ] ZenML
- [ ] Argo Workflows
- [ ] DAGs concept

## 9.8 Feature Stores 🟢

- [ ] Feast (open source)
- [ ] Tecton
- [ ] Hopsworks
- [ ] Feature store concepts: online vs offline, point-in-time correctness

## 9.9 Monitoring & Observability 🟡

- [ ] Metrics: Prometheus + Grafana
- [ ] Logging: ELK stack, Loki, Datadog
- [ ] Tracing: OpenTelemetry, Jaeger
- [ ] ML-specific: data drift, concept drift, prediction drift, label drift
- [ ] Tools: Evidently AI, Arize, WhyLabs, Fiddler, Aporia, Great Expectations
- [ ] LLM observability: LangSmith, Langfuse, Helicone, Arize Phoenix, Weave (W&B)
- [ ] Cost monitoring

## 9.10 CI/CD for ML 🟡

- [ ] GitHub Actions
- [ ] GitLab CI
- [ ] Jenkins
- [ ] ArgoCD (GitOps)
- [ ] Continuous training (CT)
- [ ] Model testing in CI: schema, performance, fairness
- [ ] Canary, blue-green, shadow deployments
- [ ] A/B testing infrastructure

## 9.11 Infrastructure as Code 🟢

- [ ] Terraform
- [ ] Pulumi
- [ ] AWS CDK
- [ ] CloudFormation

## 9.12 Distributed Training 🟢🔵

- [ ] Data parallelism: DDP, FSDP
- [ ] Tensor parallelism (Megatron-style)
- [ ] Pipeline parallelism
- [ ] Sequence parallelism
- [ ] DeepSpeed (ZeRO stages 1/2/3)
- [ ] FairScale, FSDP in PyTorch
- [ ] NCCL (GPU communication)
- [ ] Slurm (HPC scheduler)
- [ ] Ray for distributed training

## 9.13 Inference Optimization 🟡

- [ ] Quantization (INT8, INT4, FP8)
- [ ] Distillation
- [ ] Pruning
- [ ] Operator fusion
- [ ] ONNX Runtime
- [ ] TensorRT
- [ ] OpenVINO (Intel)
- [ ] Apple Core ML, Metal
- [ ] WebGPU, ONNX.js (browser)
- [ ] Edge deployment: TFLite, PyTorch Mobile

## 9.14 Hardware Awareness 🟡

- [ ] GPU architecture basics (CUDA cores, Tensor cores, memory)
- [ ] Common GPUs: A100, H100, H200, B200, L4, L40S, consumer (3090, 4090, 5090)
- [ ] TPUs (Google)
- [ ] Inferentia, Trainium (AWS)
- [ ] CUDA, cuDNN basics
- [ ] Triton (writing custom kernels) 🔵
- [ ] Profiling GPU code: Nsight, PyTorch Profiler

---

# Part 10: Advanced & Adjacent

## 10.1 AI Safety & Alignment 🟢

- [ ] Alignment problem (specification, robustness, scalable oversight)
- [ ] RLHF, Constitutional AI
- [ ] Red teaming
- [ ] Jailbreaks and defenses
- [ ] Prompt injection
- [ ] Eval harnesses for safety

## 10.2 Interpretability 🟢

- [ ] Feature importance: permutation, SHAP, LIME
- [ ] Partial dependence plots, ICE plots
- [ ] Counterfactual explanations
- [ ] Attention visualization (note: attention ≠ explanation)
- [ ] Mechanistic interpretability 🔵
- [ ] Sparse autoencoders (SAEs) for LLMs
- [ ] Activation patching, causal interventions
- [ ] Circuits (Anthropic interpretability work)

## 10.3 Fairness & Ethics 🟢

- [ ] Sources of bias in ML
- [ ] Fairness metrics: demographic parity, equalized odds, equal opportunity
- [ ] Tradeoffs between fairness definitions
- [ ] Mitigation: pre-processing, in-processing, post-processing
- [ ] Tools: AIF360, Fairlearn
- [ ] Ethics frameworks
- [ ] Regulatory awareness: EU AI Act, GDPR

## 10.4 Privacy & Security 🟢

- [ ] Differential privacy
- [ ] Federated learning
- [ ] Homomorphic encryption (concept)
- [ ] Secure multi-party computation (concept)
- [ ] Membership inference attacks
- [ ] Model extraction attacks
- [ ] Adversarial examples: FGSM, PGD
- [ ] Robust training

## 10.5 Other Architectures & Topics 🔵

- [ ] Graph Neural Networks: GCN, GAT, GraphSAGE, GIN, message passing
- [ ] Geometric deep learning
- [ ] Equivariant networks
- [ ] Neural ODEs
- [ ] Energy-based models
- [ ] Capsule networks
- [ ] Spiking neural networks
- [ ] Hyperdimensional computing

## 10.6 Causal Inference 🟢

- [ ] Correlation vs causation
- [ ] RCTs (randomized controlled trials)
- [ ] Observational studies, confounding
- [ ] Propensity score matching
- [ ] Instrumental variables
- [ ] Difference-in-differences
- [ ] DAGs (Directed Acyclic Graphs) for causality (Pearl)
- [ ] do-calculus 🔵

## 10.7 Recommender Systems 🟢

- [ ] Collaborative filtering: user-based, item-based
- [ ] Matrix factorization (SVD, ALS, NMF)
- [ ] Content-based filtering
- [ ] Hybrid approaches
- [ ] Two-tower models
- [ ] Deep learning approaches: DLRM, DCN, Wide & Deep, DeepFM
- [ ] Ranking: pointwise, pairwise, listwise
- [ ] Cold-start problem
- [ ] Implicit feedback
- [ ] Libraries: Surprise, implicit, TensorFlow Recommenders, RecBole

## 10.8 Time Series 🟢

- [ ] Components: trend, seasonality, residual
- [ ] Stationarity, ADF test
- [ ] ARIMA, SARIMA, SARIMAX
- [ ] Exponential smoothing (ETS)
- [ ] Prophet (Meta)
- [ ] NeuralProphet
- [ ] LSTM/GRU for time series
- [ ] Temporal Fusion Transformer (TFT)
- [ ] N-BEATS, N-HiTS
- [ ] TimesFM, Chronos, Moirai (foundation models for time series)
- [ ] Anomaly detection in time series
- [ ] Multi-horizon forecasting

## 10.9 Research Skills 🟡

- [ ] Reading papers efficiently (skim → deep read → reproduce)
- [ ] arXiv, Papers with Code, Semantic Scholar, Connected Papers, alphaxiv
- [ ] Following conferences: NeurIPS, ICML, ICLR, ACL, EMNLP, CVPR, ECCV
- [ ] Writing your own paper / blog post
- [ ] Citation managers: Zotero
- [ ] Reproducibility (env files, seeds, data hashes)

---

# Part 11: Career & Soft Skills

## 11.1 Portfolio 🔴

- [ ] GitHub: pinned repos, clean READMEs, good commit history
- [ ] 4–6 substantial projects (varied, ideally with one deployed)
- [ ] Live demos (Hugging Face Spaces, Streamlit Cloud, Render)
- [ ] Personal website / blog
- [ ] Kaggle profile (aim for a medal eventually)
- [ ] Hugging Face profile (models, datasets, spaces)

## 11.2 Writing & Visibility 🟡

- [ ] Technical blog posts (Medium, Substack, own site, dev.to)
- [ ] LinkedIn presence (write, don't just lurk)
- [ ] X / Twitter for ML community
- [ ] Open source contributions (start small: docs, then fixes)
- [ ] Talks at meetups
- [ ] Newsletters worth subscribing to: The Batch (Andrew Ng), Import AI (Jack Clark), Sebastian Raschka's, Lil'Log

## 11.3 Coding Interviews 🔴

- [ ] LeetCode patterns: arrays/strings, hash maps, two pointers, sliding window
- [ ] Trees and graphs: DFS, BFS, topological sort
- [ ] Dynamic programming (top patterns)
- [ ] Sorting and searching
- [ ] Heaps, tries
- [ ] Aim for ~150 problems across patterns
- [ ] NeetCode 150 list is a good guided path

## 11.4 ML-Specific Interviews 🔴

### Concepts (be able to explain to a 10-year-old)
- [ ] Bias-variance tradeoff
- [ ] Overfitting and how to prevent it
- [ ] Regularization (L1 vs L2)
- [ ] How does backprop work
- [ ] How does attention work
- [ ] What is a transformer
- [ ] Bagging vs boosting
- [ ] Why is accuracy a bad metric
- [ ] Precision vs recall (when to optimize which)
- [ ] Cross-validation strategies

### ML System Design (huge in interviews)
- [ ] Recommender system (YouTube, Netflix)
- [ ] News feed ranking
- [ ] Fraud detection
- [ ] Search ranking
- [ ] Ads ranking
- [ ] RAG / chatbot system
- [ ] Image classification at scale
- [ ] End-to-end pipeline design
- [ ] Online vs offline metrics
- [ ] Resources: *Machine Learning System Design Interview* (Aminian, Xu), Educative, ByteByteGo

### Math/Stats Questions
- [ ] Common puzzles
- [ ] Probability brain teasers
- [ ] Bayesian reasoning under interview pressure

## 11.5 Job Search 🔴

- [ ] Resume tailored to AI/ML
- [ ] LinkedIn optimization
- [ ] Where to apply: LinkedIn, AI-specific job boards (AI/ML Jobs, Cryptojobs for ML, levels.fyi), company sites
- [ ] Cold outreach to recruiters and hiring managers
- [ ] Referrals (huge) — build a network early
- [ ] Negotiation basics

## 11.6 Continuous Learning 🟡

- [ ] Allocate 1 paper a week minimum
- [ ] Re-implement one paper a month
- [ ] Follow lab blogs: Anthropic, OpenAI, DeepMind, Meta AI, Google Research, HF
- [ ] Podcasts: Machine Learning Street Talk, Latent Space, Practical AI, TWIML, Cognitive Revolution
- [ ] Discord servers: HuggingFace, EleutherAI, fast.ai, Latent Space

---

## Key Resources by Category

### Foundational Books
- *Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow* — Aurélien Géron
- *Deep Learning* — Goodfellow, Bengio, Courville (free online)
- *Mathematics for Machine Learning* — Deisenroth, Faisal, Ong (free PDF)
- *Pattern Recognition and Machine Learning* — Bishop (classic, mathy)
- *The Elements of Statistical Learning* — Hastie, Tibshirani, Friedman (free PDF)
- *Probabilistic Machine Learning* — Kevin Murphy (free PDF, three books)
- *Designing Machine Learning Systems* — Chip Huyen
- *Machine Learning Engineering* — Andriy Burkov
- *AI Engineering* — Chip Huyen (newer)
- *Build a Large Language Model (From Scratch)* — Sebastian Raschka
- *Dive into Deep Learning* (d2l.ai) — interactive book

### Courses
- Andrew Ng's *Machine Learning Specialization* (Coursera)
- Andrew Ng's *Deep Learning Specialization*
- fast.ai *Practical Deep Learning for Coders*
- Andrej Karpathy *Neural Networks: Zero to Hero* (YouTube — DO THIS)
- Andrej Karpathy *LLM 101n* (when available)
- Stanford CS229, CS230, CS231n, CS224n, CS336 (lectures on YouTube)
- Hugging Face courses (free): NLP, RL, Audio, Diffusion, Agents

### YouTube
- 3Blue1Brown (math intuition)
- StatQuest with Josh Starmer (ML intuition)
- Andrej Karpathy
- Yannic Kilcher (paper explanations)
- Aleksa Gordić (The AI Epiphany)
- Umar Jamil (deep dives, builds from scratch)

### Practice
- Kaggle (competitions, datasets, notebooks)
- Hugging Face Spaces
- Papers with Code

---

## Final Note

**This document is a map, not a destination.** Don't try to learn everything. Use it to:
1. Know what exists (so terms aren't intimidating)
2. Find the next thing to learn when ready
3. Trace why something matters (look at what comes before and after it)
4. Track progress without losing the forest for the trees

When in doubt, **build something** rather than learn more theory. Bring questions and code to me — I'll help you go deep wherever you need.
