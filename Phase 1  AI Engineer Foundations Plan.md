# Phase 1: Real Foundations — 16-Week Deep-Dive Plan

**Goal:** Go from "I build AI software with Cursor" to "I understand the math and code under every model I use."
**Duration:** 16 weeks (about 4 months)
**Time budget:** 15–20 hours per week (for example, 2 hours each weekday and 5–8 hours across the weekend)
**Final milestone:** A neural network built from scratch in NumPy, trained on MNIST to over 97% accuracy, served through FastAPI with a Next.js front end. You must be able to explain every equation and every line.

---

## How each week works

Each week has three tracks that run side by side:

| Track | Share of time | Purpose |
|---|---|---|
| Engineering (Python, NumPy, CS) | ~50% | Become a real Python engineer, not a prompt-driven one |
| Math | ~35% | Build intuition first, then formulas, then code |
| Data structures and algorithms (DSA) | ~15% | 3 problems per week; interviews and clear thinking |

**Every week ends with a build.** Each build is a small project pushed to GitHub with a README explaining what you learned.

### Rules for Phase 1

1. **No AI autocomplete on learning projects.** Turn off Cursor Tab for anything in this plan. Use AI chat only to explain errors or to review code after you've written it.
2. **The explain-back test.** Before moving on, explain the topic out loud or in writing as if teaching a junior developer. If you get stuck, you haven't learned it yet.
3. **Math by hand, then in code.** Derive it on paper first, then implement it in NumPy, then check it against a library.
4. **Predict before you run.** Before running code, write down what you expect to happen. Being wrong is where you learn the most.
5. **Keep a learning log.** Write one short entry per day: what you learned, what confused you, and what you'll do next.

---

## Week 0: Setup (2–3 days)

- Install **uv** (Python versions, virtual environments, dependencies), **ruff** (linting and formatting), **mypy** or **pyright** (type checking), **pytest**, **pre-commit**, and **Jupyter** (inside VS Code is fine).
- Create one GitHub repository, `ai-foundations`, with a folder per week.
- Set up a template project: `pyproject.toml`, `src/` layout, `tests/`, and a GitHub Actions workflow that runs ruff, mypy and pytest on every push.
- Get the core resources (see the list at the end).

**Why this matters:** most ML code in the wild is messy. Engineers who write clean, tested, typed Python stand out immediately.

---

## Block A: Python in depth + linear algebra (weeks 1–4)

### Week 1: How Python thinks (vs TypeScript)

**Engineering**
- Everything is an object. Variables are names bound to objects, not boxes holding values.
- Mutable vs immutable types; references, aliasing, shallow vs deep copy. This is the most common source of hidden bugs for TypeScript developers.
- The Python data model: `__repr__`, `__eq__`, `__hash__`, `__len__`, `__iter__`, `__getitem__`, `__add__`, `__mul__`.
- How dicts and sets work (hashing), and why lists, tuples and dicts each have their own use.
- Reading: "Fluent Python", chapters 1–3 and 6.

**Math: vectors**
- 3Blue1Brown "Essence of Linear Algebra", episodes 1–4: vectors, linear combinations, span, basis, and linear transformations as matrices.

**Build: a `Vector` class in pure Python**
- Support `+`, `-`, scalar `*`, dot product, norm, `len`, iteration, equality and hashing, with tests for each.
- README question to answer: "Why does Python call `__add__` when I write `a + b`?"

**DSA:** arrays and hashing (3 problems).

### Week 2: Functions, iterators and generators

**Engineering**
- First-class functions, closures, and scope (LEGB rule).
- Decorators: write `@timer`, `@retry` and `@cache` yourself, then compare with `functools.lru_cache`, `functools.wraps` and `functools.partial`.
- List, dict and set comprehensions vs loops.
- Iterators, generators, `yield`, `yield from`, and `itertools`.
- Reading: "Fluent Python", chapters on functions, decorators and closures, and iterators and generators.

**Math: matrices**
- 3Blue1Brown episodes 5–8: matrix multiplication as composition, determinant, inverse, rank, column space and null space.

**Build: a streaming batch loader**
- A generator that reads a large CSV file in batches with optional shuffling, without loading the whole file into memory. This is a simplified PyTorch `DataLoader`.
- Measure memory use against a version that loads everything into a list.

**DSA:** two pointers and sliding window.

### Week 3: Object-oriented design, typing and errors

**Engineering**
- Classes, `@dataclass`, `@property`, class vs instance attributes, inheritance vs composition.
- Abstract base classes and `typing.Protocol` (the closest equivalent of TypeScript interfaces).
- Type hints in depth: generics, `TypeVar`, `Literal`, `TypedDict`, `Callable`, `Optional`. Run mypy in strict mode.
- Pydantic v2 models (you know these from FastAPI; now learn how validation actually works).
- Exceptions, custom error classes, and context managers (`with`, `__enter__`/`__exit__`, `contextlib`).

**Math: geometry of linear algebra**
- 3Blue1Brown episodes 9–14: dot products, change of basis, eigenvectors and eigenvalues.
- "Mathematics for Machine Learning" (MML book), chapter 2.

**Build: a `Matrix` class in pure Python**
- Fully typed: matrix multiply (with `@`, via `__matmul__`), transpose, identity, determinant (2×2 and 3×3), and matrix–vector multiply using your `Vector` class.
- Test it against NumPy results.

**DSA:** stacks and binary search.

### Week 4: Concurrency, performance and FastAPI in depth

**Engineering**
- The GIL (Global Interpreter Lock): what it is and why it exists. Threading vs multiprocessing vs asyncio, and when to use each.
- `asyncio` compared with the Node.js event loop: `async`/`await`, `gather`, semaphores, timeouts.
- Profiling: `timeit`, `cProfile`, `line_profiler`, and memory profiling.
- FastAPI in depth: sync vs async endpoints (and what happens when you block the event loop), dependency injection, lifespan events, background tasks, middleware, and testing with `TestClient`/`httpx`.

**Math: analytic geometry**
- MML book chapter 3: norms, inner products, distances, angles, orthogonality and projections.
- Key connection: cosine similarity, which you already use in RAG, is just a normalized dot product.

**Build: an async LLM gateway in FastAPI**
- Accept a batch of prompts, call an LLM API concurrently with a semaphore-based rate limit, retries with exponential backoff, and timeouts.
- Benchmark sequential vs concurrent calls, and profile to find the slowest part.

**DSA:** linked lists.

**Block A checkpoint:** can you explain, without notes, mutability, decorators, generators, the GIL, and what a matrix does to space geometrically?

---

## Block B: NumPy, data and calculus (weeks 5–8)

### Week 5: NumPy in depth

**Engineering**
- The `ndarray`: shape, dtype, strides, and contiguous memory.
- Views vs copies (a major source of silent bugs).
- Vectorization: why NumPy is often 50–100× faster than Python loops.
- Broadcasting rules. Learn them until you can predict output shapes in your head.
- Indexing: fancy indexing, boolean masks, `np.where`, `np.einsum` (introduction).
- Reading: "Python Data Science Handbook" (Jake VanderPlas, free online), NumPy chapter.

**Math: matrix decompositions**
- MML book chapter 4: eigendecomposition and singular value decomposition (SVD). Watch the 3Blue1Brown eigenvector video again.

**Build: vectorized similarity search**
- Generate 100,000 random "embeddings" with 384 dimensions. Implement top-k cosine similarity search with a Python loop, then fully vectorized.
- Benchmark both. Rewrite your Week 3 `Matrix` operations in NumPy and compare speed.

**DSA:** trees (traversals).

### Week 6: Working with real data

**Engineering**
- pandas: loading data, cleaning, missing values, `groupby`, `merge`, pivots, time series basics. Look at Polars as a faster modern alternative.
- Visualization with Matplotlib and Seaborn: histograms, scatter plots, correlation heatmaps.
- Exploratory data analysis (EDA) as a habit: always look at the data before modeling.

**Math: dimensionality reduction**
- Principal component analysis (PCA): what it is geometrically and why SVD computes it (MML book chapter 10).

**Build: EDA + PCA from scratch**
- Pick a real dataset (housing prices, or something from your own SaaS domain). Clean it, explore it, and write up findings.
- Implement PCA with NumPy SVD, project the data to 2D and plot it, then compare with scikit-learn's `PCA`.

**DSA:** trees (BST, depth-first and breadth-first search).

### Week 7: Calculus for ML

**Math (main focus this week)**
- 3Blue1Brown "Essence of Calculus": derivatives, the chain rule, and the intuition behind them.
- Partial derivatives, gradients, the Jacobian, and an introduction to the Hessian (MML book chapter 5).
- The chain rule on computation graphs. This is backpropagation, and the most important idea in Phase 1.

**Engineering**
- Numerical differentiation (finite differences) vs analytical derivatives.
- Floating-point precision and why the step size matters.

**Build: a gradient-checker utility**
- A function that computes numerical gradients of any function, plus analytical gradients for 5 functions you derive by hand (including `sigmoid`, `tanh` and the squared-error loss). Check that they match.
- You will reuse this tool in the final project.

**DSA:** heaps and priority queues.

### Week 8: Optimization

**Math**
- Gradient descent, learning rates, convex vs non-convex functions, local minima and saddle points.
- Stochastic and mini-batch gradient descent, momentum, RMSProp and Adam: what each fixes and why.
- MML book chapter 7.

**Build: an optimizer lab + linear regression from scratch**
- Implement GD, SGD, momentum and Adam in NumPy. Minimize the Rosenbrock function and plot each optimizer's path.
- Implement linear regression two ways: the closed-form normal equation, and gradient descent. Compare results and running time with scikit-learn's `LinearRegression`.

**DSA:** graphs (introduction).

**Block B checkpoint:** can you derive the gradient of the mean squared error loss for linear regression on paper, implement it vectorized, and explain why Adam usually converges faster than plain SGD?

---

## Block C: Probability, statistics and first ML models (weeks 9–12)

### Week 9: Probability

**Math**
- Random variables; Bernoulli, binomial, categorical and Gaussian distributions.
- Expectation, variance, covariance; joint, marginal and conditional probability; independence.
- Bayes' theorem, with real intuition.
- Resources: StatQuest videos and MML book chapter 6.

**Engineering**
- Simulation with `np.random.default_rng`: check theory against experiment (law of large numbers, central limit theorem).

**Build: Naive Bayes spam classifier from scratch**
- Tokenize text, compute probabilities with Laplace smoothing, and work in log space to avoid underflow. Compare with scikit-learn.

**DSA:** graphs (BFS/DFS problems).

### Week 10: Statistics and information theory

**Math**
- Maximum likelihood estimation (MLE) and maximum a posteriori (MAP) estimation. Show that MAP with a Gaussian prior equals L2 regularization.
- Information theory: entropy, cross-entropy and KL divergence. Why cross-entropy is the standard loss for classification, and the loss LLMs are trained on.
- Confidence intervals, hypothesis testing, and the bootstrap. You'll need these for honest model evaluation later.

**Build: logistic regression from scratch**
- Derive the cross-entropy gradient by hand, implement it in NumPy, verify it with your Week 7 gradient checker, add L2 regularization, and train it on a real binary classification dataset.

**DSA:** dynamic programming (introduction).

### Week 11: Classical ML fundamentals

**ML concepts**
- Train, validation and test splits; data leakage (the classic beginner mistake).
- Bias–variance tradeoff, underfitting vs overfitting, L1 vs L2 regularization.
- Cross-validation and hyperparameter search.
- Metrics: accuracy, precision, recall, F1, ROC-AUC, confusion matrices, and when accuracy misleads.
- Andrew Ng's Machine Learning Specialization, course 1 and the relevant parts of course 2.

**Build: model comparison report**
- On one dataset, compare your from-scratch linear and logistic regression with scikit-learn models (logistic regression, random forest, gradient boosting).
- Use proper cross-validation and write an honest evaluation report: which model wins, by how much, and how confident you are.

**DSA:** dynamic programming.

### Week 12: How computers run ML code

**CS fundamentals**
- The memory hierarchy (registers, cache, RAM, disk) and why memory access patterns affect speed.
- CPU vs GPU: why GPUs are fast at matrix multiplication (parallelism and memory bandwidth). This is a conceptual preview of Phase 3.
- Floating point: float32, float16 and bfloat16, overflow, underflow and precision loss. This explains why quantization and mixed precision matter.
- Big-O complexity for common ML operations (for example, why attention scales as O(n²) with sequence length).

**Build: numerical-stability lab**
- Show a naive softmax overflowing, then implement the numerically stable version and the log-sum-exp trick.
- Show float16 precision loss on a sum. Write a short explanation of why this matters when training neural networks.

**DSA:** mixed review.

**Block C checkpoint:** can you explain why cross-entropy is the right loss for classification using MLE, and spot data leakage in someone else's notebook?

---

## Block D: Capstone (weeks 13–16)

### Week 13: Neural network from scratch, part 1

- Design a small, modular library in NumPy: `Linear` layer, `ReLU`, `Sigmoid` and `Tanh` activations, softmax combined with cross-entropy loss, each with `forward` and `backward` methods.
- Derive backpropagation for each layer on paper first. Verify every `backward` with your gradient checker.
- Weight initialization (Xavier/He): try training without it and see what goes wrong.

### Week 14: Neural network from scratch, part 2

- Mini-batch training loop with your Week 8 optimizers (SGD, momentum, Adam).
- Train on MNIST and reach over 97% test accuracy.
- Add learning-rate schedules, early stopping, and training/validation loss curves.
- Diagnose problems deliberately: set the learning rate too high, initialize badly, overfit a tiny subset. Document what each failure looks like.

### Week 15: Autograd engine + production packaging

- Work through Andrej Karpathy's **micrograd** video and build your own small automatic differentiation engine. Compare it with your manual backprop: this is the bridge to how PyTorch works.
- Package your neural network library properly: typed, tested, linted, with continuous integration on GitHub Actions.
- Serve the trained MNIST model through a FastAPI endpoint. Build a small **Next.js** page where users draw a digit and get a prediction. This uses your TypeScript strength.

### Week 16: Consolidation and review

- Write a technical blog post: "I built a neural network from scratch — here's every equation." Publish it (dev.to, Medium or your own site).
- Final explain-back test: record yourself explaining backpropagation end to end, from the loss to the first layer's weights.
- Go back to the weak spots in your learning log and redo one build you found hardest.
- Rest. Phase 2 (PyTorch and LLM internals) builds directly on this.

---

## Phase 1 exit checklist

Move to Phase 2 only when you can honestly tick every item:

**Python**
- [ ] I can explain mutability, references, decorators, generators, the GIL and async without notes.
- [ ] My code is typed, tested, linted and runs in CI by default.
- [ ] I can profile slow Python code and fix it.

**Math**
- [ ] I can explain matrix multiplication, eigenvectors and SVD geometrically.
- [ ] I can apply the chain rule on a computation graph by hand.
- [ ] I can derive gradients for linear and logistic regression.
- [ ] I understand MLE, cross-entropy and KL divergence, and how they connect.

**ML and engineering**
- [ ] I've written backpropagation from scratch and verified it with gradient checking.
- [ ] I can write vectorized NumPy fluently and predict broadcasting shapes.
- [ ] I can evaluate a model honestly: proper splits, no leakage, the right metrics.
- [ ] I've deployed my own model behind an API with a working front end.

---

## Core resources (one per topic)

| Topic | Resource | Weeks |
|---|---|---|
| Python in depth | [Fluent Python, 2nd edition (Luciano Ramalho)](https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/) | 1–4 |
| Python tooling | [uv documentation](https://docs.astral.sh/uv/) | 0 |
| FastAPI and async | [FastAPI official tutorial](https://fastapi.tiangolo.com/tutorial/) | 4 |
| Linear algebra | [3Blue1Brown, Essence of Linear Algebra](https://www.3blue1brown.com/lessons/vectors/) | 1–5 |
| Calculus | [3Blue1Brown, Essence of Calculus](https://www.3blue1brown.com/lessons/essence-of-calculus/) | 7 |
| Math for ML (written practice) | [Mathematics for Machine Learning (free book)](https://mml-book.github.io/) | 3–10 |
| Probability and statistics | [StatQuest video index](https://statquest.org/video_index.html) | 9–10 |
| NumPy and pandas | [Python Data Science Handbook (free online)](https://jakevdp.github.io/PythonDataScienceHandbook/) | 5–6 |
| Classical ML | [Andrew Ng, Machine Learning Specialization](https://www.coursera.org/specializations/machine-learning-introduction) | 11 |
| Floating point | [Python docs: Floating-Point Arithmetic](https://docs.python.org/3/tutorial/floatingpoint.html) | 12 |
| Neural networks and backprop | [Andrej Karpathy, Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html) | 13–15 |
| Data structures and algorithms | [NeetCode roadmap](https://neetcode.io/roadmap) | 1–16 |

## Common traps to avoid

- **Watching instead of building.** For every hour of video, spend at least two hours writing code.
- **Getting stuck on math perfection.** Aim for working intuition plus the ability to derive the key results. Deeper proofs can wait.
- **Skipping tests on "learning code."** Tests are how you prove your implementation is correct, especially for gradients.
- **Comparing yourself to others online.** Measure yourself only against the exit checklist.
- **Letting Cursor do the thinking.** The whole point of Phase 1 is that you do the hard part.
