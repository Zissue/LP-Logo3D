# Contributing to Logo3D

Thank you for your interest in contributing to Logo3D! This document provides guidelines for contributing to the project.

## How to Contribute

### Reporting Bugs

If you find a bug, please open an issue with:
- A clear description of the problem
- Steps to reproduce the issue
- Expected vs. actual behavior
- Your environment (OS, Python version, VPython version)
- Sample Logo3D code that demonstrates the bug

### Suggesting Enhancements

Enhancement suggestions are welcome! Please open an issue describing:
- The enhancement you'd like to see
- Why it would be useful
- How it might work

### Contributing Code

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/my-new-feature`
3. **Make your changes**
4. **Test your changes**: Run existing test programs to ensure nothing breaks
5. **Commit your changes**: `git commit -am 'Add new feature'`
6. **Push to the branch**: `git push origin feature/my-new-feature`
7. **Submit a pull request**

## Development Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Zissue/LP-Logo3D.git
   cd LP-Logo3D
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Install ANTLR4:
   - Follow the [official installation guide](https://github.com/antlr/antlr4/blob/master/doc/getting-started.md#installation)

4. Compile the grammar:
   ```bash
   antlr4 -Dlanguage=Python3 -no-listener -visitor logo3d.g
   ```

5. Test the installation:
   ```bash
   python3 logo3d.py inputs_tests/espiral.l3d
   ```

## Code Style

### Python Code
- Follow PEP 8 style guidelines
- Use meaningful variable and function names
- Add docstrings to classes and methods
- Keep functions focused and small

### Logo3D Code
- Use clear procedure names
- Add comments to explain complex logic
- Format code consistently (indentation, spacing)

## Testing

When adding new features or fixing bugs:

1. **Test existing programs**: Ensure your changes don't break existing functionality
   ```bash
   python3 logo3d.py inputs_tests/espiral.l3d
   python3 logo3d.py inputs_tests/cube.l3d
   python3 logo3d.py inputs_tests/pyramid.l3d
   ```

2. **Create new test programs**: Add Logo3D test files in `inputs_tests/` demonstrating your feature or bug fix

3. **Visual verification**: Check that 3D output renders correctly in VPython

## Areas for Contribution

### Language Features
- New turtle commands (e.g., `circle()`, `arc()`)
- Additional control structures
- Functions/procedures with return values
- Arrays or lists
- String manipulation

### Interpreter Improvements
- Better error messages
- Runtime debugging support
- Performance optimizations
- Memory management improvements

### Documentation
- More example programs
- Tutorial for beginners
- Language specification
- API documentation
- Screenshots and videos

### Tooling
- Syntax highlighting for editors
- IDE integration
- Debugger
- Unit tests
- Continuous integration

### Graphics Enhancements
- Export to image/video files
- Custom shapes and objects
- Textures and materials
- Lighting controls
- Animation recording

## Grammar Changes

If modifying `logo3d.g`:

1. Test thoroughly with various programs
2. Update documentation to reflect changes
3. Recompile with ANTLR4
4. Test that generated parser/lexer work correctly

## Commit Messages

Write clear, concise commit messages:
- Use present tense: "Add feature" not "Added feature"
- First line: brief summary (50 chars or less)
- Followed by blank line and detailed description if needed
- Reference issues: "Fixes #123" or "Related to #456"

Examples:
```
Add circle command for turtle graphics

Implement circle(radius, steps) command that draws
a circle using forward and left commands.

Fixes #42
```

## Pull Request Process

1. Update README.md if adding features visible to users
2. Update ARCHITECTURE.md if changing internal structure
3. Add test programs demonstrating new functionality
4. Ensure all existing tests still pass
5. Request review from maintainers

## Questions?

If you have questions about contributing:
- Open an issue for discussion
- Check existing issues and pull requests
- Review the documentation

## License

By contributing, you agree that your contributions will be licensed under the same license as the project (if specified).

Thank you for contributing to Logo3D! 🎨🐢🎉
