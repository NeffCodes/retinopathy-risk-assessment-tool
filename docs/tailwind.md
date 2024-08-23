# Tailwind With Django

## Overview

This document is to provide information on installation and usage for Tailwind CSS.
Tailwind will build out the css file so we don't have to worry about running any commands for it to be active when launching our server.

## Making Style Changes

If  you are making style changes to the templates in this project, you can run the following steps in the root `rrat` directory.

1. Ensure you have all the dependencies installed

  ```bash
  npm install
  ```

2. Run the Tailwind Build command

  ```bash
  npm run build:css
  ```

This will run the build command for Tailwind with a `--watch` flag which will auto rebuild whenever we modify the `input.css` or any HTML Template. You can also run the following command the one above doesn't work:

  ```bash
  npx tailwindcss -i ./static/css/input.css -o ./static/css/output.css --watch
  ```

## Installation

You shouldn't need to install Tailwind into this project since I have it set up as a dependency.

### Fresh Installation

If you are looking to install a fresh installation of tailwind into a separate project, you would follow these steps:

#### Prerequisites

- [Node 16.17 or higher](https://nodejs.org/en)

#### Steps

1. Navigate to your project folder

```bash
cd your-project
```

2. Initialize a new npm project:

```bash
npm init -y
```

3. Install Tailwind.css

```bash
npm install tailwindcss postcss autoprefixer
```

4. Generate Tailwind config

```bash
npx tailwindcss init
```

#### Tailwind with Django

If you are wanting to integrate tailwind with django, you would do the following steps after you setup Tailwindcss following the steps above.

1. Update the `tailwind.config.js` file to specify where Tailwind should look for content. Modify it to include the paths to your Django templates.

```js
module.exports = {
  content: [
    './templates/**/*.html',
    './static/**/*.js',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

2. In your `static` folder (e.g. `static/css`), create a file called `input.css`

```bash
mkdir -p static/css
touch static/css/input.css
```

3. In `input.css`, add the following:

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

4. Run the following command to build your tailwind css. 
This will generate the output.css file, which you’ll use in your templates.

```bash
npx tailwindcss -i ./static/css/input.css -o ./static/css/output.css --watch
```

5. Include Tailwind CSS in Django Templates. 
In your base template (e.g., base.html), link the output.css file:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="{% static 'css/output.css' %}" rel="stylesheet">
    <title>Your Django App</title>
  </head>
  <body>
    {% block content %}
    {% endblock %}
  </body>
</html>

```

6. You can now use Tailwind CSS classes in Django Templates!

```html
<div class="p-4 bg-blue-500 text-white">
  Hello, Tailwind with Django!
</div>
```