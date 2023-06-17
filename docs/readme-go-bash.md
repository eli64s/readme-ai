
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>
cache
</h1>
<h3 align="center">📍 Put your code in Cache for maximum performance!</h3>
<h3 align="center">🚀 Developed with the software and tools below.</h3>
<p align="center">

<img src="https://img.shields.io/badge/Markdown-000000.svg?style=for-the-badge&logo=Markdown&logoColor=white" alt="" />
<img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=for-the-badge&logo=GNU-Bash&logoColor=white" alt="idx" />
<img src="https://img.shields.io/badge/Go-00ADD8.svg?style=for-the-badge&logo=Go&logoColor=white" alt="md" />
</p>

</div>

---
## 📚 Table of Contents
- [📚 Table of Contents](#-table-of-contents)
- [📍Overview](#-introdcution)
- [🔮 Features](#-features)
- [⚙️ Project Structure](#project-structure)
- [🧩 Modules](#modules)
- [🏎💨 Getting Started](#-getting-started)
- [🗺 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [🪪 License](#-license)
- [📫 Contact](#-contact)
- [🙏 Acknowledgments](#-acknowledgments)

---

## 📍Overview

GitHub project cache is a powerful tool that stores project data as well as release files, allowing users to quickly access their projects and project data. Furthermore, users can access any previous version of the project,

## 🔮 Feautres

> `[📌  INSERT-PROJECT-FEATURES]`

---

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-github-open.svg" width="80" />

## ⚙️ Project Structure

```bash
.
├── LICENSE
├── README.md
├── benchmark_test.go
├── cache.go
├── example
│   └── main.go
├── filter.go
├── filter_test.go
├── go.mod
├── hash.go
├── hash_test.go
├── local.go
├── local_test.go
├── lru.go
├── lru_test.go
├── policy.go
├── policy_test.go
├── sketch.go
├── sketch_test.go
├── stats.go
├── stats_test.go
├── synthetic
│   ├── counter.go
│   ├── exponential.go
│   ├── hotspot.go
│   ├── synthetic.go
│   ├── uniform.go
│   └── zipf.go
├── tinylfu.go
├── tinylfu_test.go
└── traces
    ├── README.md
    ├── address.go
    ├── address_test.go
    ├── cache2k.go
    ├── cache2k_test.go
    ├── combine-png.sh
    ├── combine.sh
    ├── dl-address.sh
    ├── dl-cache2k.sh
    ├── dl-storage.sh
    ├── dl-wikipedia.sh
    ├── dl-youtube.sh
    ├── files.go
    ├── report.go
    ├── report.png
    ├── report.sh
    ├── report_test.go
    ├── storage.go
    ├── storage_test.go
    ├── visualize-request.sh
    ├── visualize-size.sh
    ├── wikipedia.go
    ├── wikipedia_test.go
    ├── youtube.go
    ├── youtube_test.go
    ├── zipf.go
    └── zipf_test.go

4 directories, 55 files
```
---

<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-src-open.svg" width="80" />

## 💻 Modules
<details closed><summary>Example</summary>

| File    | Summary                                                                                                                    | Module          |
|:--------|:---------------------------------------------------------------------------------------------------------------------------|:----------------|
| main.go | This code creates a cache with a maximum size of 1000, an expiration time of 30 seconds, and a refresh time of 20 seconds. | example/main.go |

</details>

<details closed><summary>Root</summary>

| File              | Summary                                                                                                                                                                                                                                                                                                                                         | Module            |
|:------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------|
| go.mod            | Goburrow/cache is a Go module for caching data in memory. It provides an easy-to-use API for storing and retrieving data with support for expiration, eviction, and thread-safety.                                                                                                                                                              | go.mod            |
| local_test.go     | Error fetching summary.                                                                                                                                                                                                                                                                                                                         | local_test.go     |
| filter_test.go    | This code tests a bloom filter package by initializing it with a given number of inputs and a false positive rate, then checking if the filter contains the inputs and if it returns the correct values for existing and non-existing inputs.                                                                                                   | filter_test.go    |
| policy_test.go    | This code benchmarks a cache package by creating entries, getting or setting them, and deleting them. It uses atomic operations and runs in parallel to measure performance.                                                                                                                                                                    | policy_test.go    |
| lru_test.go       | This code is a package for testing a cache, specifically an LRU (Least Recently Used) cache and a Segmented LRU (SLRU) cache.                                                                                                                                                                                                                   | lru_test.go       |
| policy.go         | Package cache is a data structure for storing cache entries with a cache policy. It includes functions for getting, setting, and deleting entries, as well as functions for managing the cache policy.                                                                                                                                          | policy.go         |
| cache.go          | Package cache provides partial implementations of Guava Cache, including support for LRU, Segmented LRU and TinyLFU. It provides functions to get, put, invalidate, and refresh values associated with keys, as well as a Reloader interface to asynchronously reload values.                                                                   | cache.go          |
| local.go          | Error fetching summary.                                                                                                                                                                                                                                                                                                                         | local.go          |
| tinylfu.go        | Package cache implements TinyLFU, a caching algorithm utilizing 4bit Count Min Sketch and Bloom Filter as a Doorkeeper and Segmented LRU for long term retention.                                                                                                                                                                               | tinylfu.go        |
| filter.go         | nextPowerOfTwo returns the next power of two for the given number. func nextPowerOfTwo(n uint32) uint32 {                                                                                                                                                                                                                                       | filter.go         |
|                   | 	n--                                                                                                                                                                                                                                                                                                                                            |                   |
|                   | 	n |= n >> 1                                                                                                                                                                                                                                                                                                                                    |                   |
|                   | 	n |= n >> 2                                                                                                                                                                                                                                                                                                                                    |                   |
|                   | 	n |= n >> 4                                                                                                                                                                                                                                                                                                                                    |                   |
|                   | 	n |= n >> 8                                                                                                                                                                                                                                                                                                                                    |                   |
|                   | 	n |= n >> 16                                                                                                                                                                                                                                                                                                                                   |                   |
|                   | 	n++                                                                                                                                                                                                                                                                                                                                            |                   |
|                   | 	return n                                                                                                                                                                                                                                                                                                                                       |                   |
|                   | }                                                                                                                                                                                                                                                                                                                                               |                   |
| hash_test.go      | This package provides functions to calculate a 64-bit hash value using the FNV algorithm for a variety of data types, including integers, strings, and booleans.                                                                                                                                                                                | hash_test.go      |
| stats.go          | This package provides a cache with performance statistics, including hit rate, miss rate, load error rate, average load penalty, and eviction count.                                                                                                                                                                                            | stats.go          |
| lru.go            | Package cache is a LRU cache and segmented LRU cache implementation. It provides functions to initialize, write, access, remove, and iterate through the cache.                                                                                                                                                                                 | lru.go            |
| hash.go           | This package provides a cache key hashing function that can be used to override the default hash function. It supports a variety of data types, including integers, floats, strings, and pointers.                                                                                                                                              | hash.go           |
| tinylfu_test.go   | This code is a test for the tinyLFU package cache, which is used to store and manage data. It includes functions to assert the capacity, length, and entries of the cache, as well as functions to write and access entries.                                                                                                                    | tinylfu_test.go   |
| benchmark_test.go | This package provides a cache with various synthetic generators for benchmarking. It includes functions for testing the maximum size, uniform, counter, exponential, zipf, and hotspot generators.                                                                                                                                              | benchmark_test.go |
| sketch_test.go    | This code tests and benchmarks a countMinSketch package, which is used to store and retrieve data from a cache. It tests the accuracy of the data stored in the cache and benchmarks the resetting of the cache.                                                                                                                                | sketch_test.go    |
| sketch.go         | This package provides an implementation of count-min sketch with 4-bit counters. It includes functions to initialize, add, estimate, reset, and clear the sketch.                                                                                                                                                                               | sketch.go         |
| stats_test.go     | This package cache code tests a statsCounter struct, recording hits, misses, load successes, load errors, and evictions. It then takes a snapshot of the stats and tests the hit count, miss count, success count, error count, total load time, eviction count, request count, hit rate, miss rate, load error rate, and average load penalty. | stats_test.go     |

</details>

<details closed><summary>Synthetic</summary>

| File           | Summary                                                                                                                                                                                                                                                               | Module                   |
|:---------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------|
| synthetic.go   | This package provides an interface for generating pseudo-random numbers. It defines the Generator interface which provides a method for generating an integer.                                                                                                        | synthetic/synthetic.go   |
| exponential.go | This package provides a Generator resembling an exponential distribution, which is initialized with a mean value and returns a random integer.                                                                                                                        | synthetic/exponential.go |
| counter.go     | This package provides a Generator which returns a sequence of unique integers, starting from a given start value. It uses the atomic package to ensure thread safety.                                                                                                 | synthetic/counter.go     |
| zipf.go        | This package provides a Generator resembling Zipf distribution, which is a type of probability distribution. It takes in three parameters: min, max, and exp, and returns a Generator with a random source seeded with the current UnixNano time.                     | synthetic/zipf.go        |
| uniform.go     | This package provides a uniformGenerator type which implements a Generator interface. It uses the math/rand package to generate random numbers within a given range (min, max).                                                                                       | synthetic/uniform.go     |
| hotspot.go     | This package provides a hotspotGenerator struct which generates random integers resembling a hotspot distribution. It takes in a minimum and maximum value, as well as a hotFrac float64 which is the fraction of total items which have a proportion (1. 0-hotFrac). | synthetic/hotspot.go     |

</details>

<details closed><summary>Traces</summary>

| File                 | Summary                                                                                                                                                                                                                                                                                                                 | Module                      |
|:---------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------|
| youtube.go           | This package provides a youtubeProvider struct which reads from an io. Reader and provides a context and keys channel. It parses the bytes read from the io.                                                                                                                                                            | traces/youtube.go           |
| files.go             | This package provides functions to open and read files with the extensions . gzand . bz2, as well as reset the reader and close the files.                                                                                                                                                                              | traces/files.go             |
| dl-storage.sh        | This code downloads two files, WebSearch1. spc. bz2 and Financial2. spc. bz2, from the skuld. cs. umass. edu/traces/storage/ directory if they are not already present.                                                                                                                                                 | traces/dl-storage.sh        |
| address_test.go      | This package traces tests the request and size of an address provider using different policies. It runs tests in parallel and uses a cache size of 128 for request tests and 25 for size tests.                                                                                                                         | traces/address_test.go      |
| address.go           | This code provides a Provider with items from application traces by the University of California, San Diego. It reads bytes from a given reader, parses them, and returns a uint64 value.                                                                                                                               | traces/address.go           |
| visualize-size.sh    | This code is a bash script that creates a graph of hit rate versus cache size from a set of data files. It sets the output format, creates a plot argument, and then uses gnuplot to create the graph.                                                                                                                  | traces/visualize-size.sh    |
| youtube_test.go      | This package traces tests the request and size of a Youtube provider using different policies. It runs tests in parallel and sets options such as cache size, report interval, and max items.                                                                                                                           | traces/youtube_test.go      |
| dl-cache2k.sh        | This code downloads six trace files from a GitHub repository and stores them in the current directory.                                                                                                                                                                                                                  | traces/dl-cache2k.sh        |
| report.sh            | This code is a Bash script that runs tests, visualizes requests, and visualizes cache sizes for a list of traces (Address, CPP, Multi2, ORMBusy, Glimpse, OLTP, Sprite, Financial, WebSearch, Wikipedia, YouTube, and Zipf).                                                                                            | traces/report.sh            |
| dl-address.sh        | This code downloads a file called "proj1-traces. tar. gz" from a website and extracts the contents of the file.                                                                                                                                                                                                         | traces/dl-address.sh        |
| storage_test.go      | This package traces code tests the request and size of web search and financial data with different policies and options.                                                                                                                                                                                               | traces/storage_test.go      |
| storage.go           | This package provides a storage provider for traces from the University of Massachusetts. It reads from an io. Reader and provides items to a channel.                                                                                                                                                                  | traces/storage.go           |
| wikipedia_test.go    | This code tests the request and size of a Wikipedia provider using different policies. It runs tests in parallel and sets options such as cache size, report interval, and max items.                                                                                                                                   | traces/wikipedia_test.go    |
| cache2k_test.go      | This package traces code tests the performance of different caching policies on various trace files. It runs tests for request and size on trace files such as trace-mt-db-*-busy. trc. bin. bz2, trace-cpp. trc. bin. gz, trace-glimpse. trc. bin. gz, trace-oltp. trc. bin. gz, trace-sprite. trc. bin. gz, and trace | traces/cache2k_test.go      |
| dl-youtube.sh        | This code downloads a file called youtube_traces. tgz, extracts it, and renames the files within it according to the date they were created.                                                                                                                                                                            | traces/dl-youtube.sh        |
| combine.sh           | This code is a shell script that creates a report in the specified format (default is png) by concatenating all files with the pattern *-requests. $FORMAT and *-cachesize. $FORMAT and saving the result as report. $FORMAT.                                                                                           | traces/combine.sh           |
| visualize-request.sh | This code is a bash script that uses gnuplot to generate a graph from a set of data files. It sets the output format, creates a plot argument from the data files, and then uses gnuplot to generate the graph with the given parameters.                                                                               | traces/visualize-request.sh |
| wikipedia.go         | This package provides a WikipediaProvider which reads from an io. Reader and parses the data to extract URLs. It then sends the URLs to a channel for further processing.                                                                                                                                               | traces/wikipedia.go         |
| report.go            | This package provides a benchmarking tool for caches, allowing users to report on the performance of their caches with various policies and cache sizes.                                                                                                                                                                | traces/report.go            |
| report_test.go       | This package provides functions to test request and size of traces. It opens files, creates a provider, creates a reporter, and benchmarks the cache.                                                                                                                                                                   | traces/report_test.go       |
| cache2k.go           | This code creates a cache2kProvider struct which reads in data from a given io. Reader and provides it to a given context.                                                                                                                                                                                              | traces/cache2k.go           |
| zipf.go              | This package provides a zipfProvider type which implements the Provider interface. It uses the rand. Zipf function to generate random numbers with a Zipf distribution, and provides a function to create a new zipfProvider with a given s and num parameter.                                                          | traces/zipf.go              |
| combine-png.sh       | This code creates a montage of four images (address-requests. png, address-cachesize. png, wikipedia-requests. png, wikipedia-cachesize. png, youtube-requests. png, youtube-cachesize. png, zipf-requests. png, zipf-cachesize. png) and saves it as a single image named report. png.                                 | traces/combine-png.sh       |
| dl-wikipedia.sh      | This code downloads the file "wiki. 1191201596. gz" from the website "http://www. wikibench. eu/wiki/2007-10/" if it is not already present in the current directory.                                                                                                                                                   | traces/dl-wikipedia.sh      |
| zipf_test.go         | This package traces tests the request and size of a Zipf provider with different policies. It creates a report file for each policy and tests the cache size and max items.                                                                                                                                             | traces/zipf_test.go         |

</details>
<hr />

## 🚀 Getting Started

### ✅ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> `[📌  INSERT-PROJECT-PREREQUISITES]`

### 💻 Installation

1. Clone the cache repository:
```sh
git clone https://github.com/goburrow/cache
```

2. Change to the project directory:
```sh
cd cache
```

3. Install the dependencies:
```sh
go build -o myapp
```

### 🤖 Using cache

```sh
./myapp
```

### 🧪 Running Tests
```sh
#run tests
```

<hr />

## 🛠 Future Development
- [X] [📌  COMPLETED-TASK]
- [ ] [📌  INSERT-TASK]
- [ ] [📌  INSERT-TASK]


---

## 🤝 Contributing
Contributions are always welcome! Please follow these steps:
1. Fork the project repository. This creates a copy of the project on your account that you can modify without affecting the original project.
2. Clone the forked repository to your local machine using a Git client like Git or GitHub Desktop.
3. Create a new branch with a descriptive name (e.g., `new-feature-branch` or `bugfix-issue-123`).
```sh
git checkout -b new-feature-branch
```
4. Make changes to the project's codebase.
5. Commit your changes to your local branch with a clear commit message that explains the changes you've made.
```sh
git commit -m 'Implemented new feature.'
```
6. Push your changes to your forked repository on GitHub using the following command
```sh
git push origin new-feature-branch
```
7. Create a pull request to the original repository.
Open a new pull request to the original project repository. In the pull request, describe the changes you've made and why they're necessary.
The project maintainers will review your changes and provide feedback or merge them into the main branch.

---

## 🪪 License

This project is licensed under the `[📌  INSERT-LICENSE-TYPE]` License. See the [LICENSE](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository) file for additional info.

---

## 🙏 Acknowledgments

[📌  INSERT-DESCRIPTION]


---
