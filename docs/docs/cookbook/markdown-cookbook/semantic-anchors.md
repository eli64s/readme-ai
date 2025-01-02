# Use Semantic Anchors: Assign meaningful id attributes to your anchors for better accessibility and readability.

Include the id attribute in the heading tag using a hyperlink tag `<a>`.

```markdown
<div align="left"><a id="top"></a>

# Section 1

# Section 2

# Section 3

</div>

<div align="left">
    <a href="#top">
        <img src="assets/button.svg" width="88px" height="88px" alt="return-button">
    </a>
</div>
```

Or include the id attribute in the div tag.

```markdown
<div id="section-1">

# Section 1

</div>

<div align="left">
    <a href="#top">
        <img src="assets/button.svg" width="88px" height="88px" alt="return-button">
    </a>
</div>
```

---
