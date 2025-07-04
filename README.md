# Slugify
A lightweight Python script to turn text into URL-friendly slugs.

## Features
- **Cleans Text**: Removes punctuation and extra spaces.
- **Formats Slugs**: Converts to lowercase, replaces spaces with single hyphens.

## Usage
```python
slugify("  Hello, World! This is PYTHON!@.  ")
# Output: "hello-world-this-is-python"
```

## Examples
```python
print(slugify(" Hello #World FROM  @IRan!"))
# Output: "hello-world-from-iran"
```

## Notes
- Handles various punctuation marks.
- Built with ❤️ by Ehsan.
