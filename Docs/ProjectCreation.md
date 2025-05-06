# Step 1: Create the base project with Supabase and TypeScript
npx create-next-app@15.3.1 cron-job -e with-supabase --ts
cd cron-job

# Step 2: Install required dependencies
npm install tailwindcss@4.1.5 postcss@latest autoprefixer@latest
npm install tremor@3.18.7
npm install @supabase/supabase-js@2.49.4
npm install eslint prettier --save-dev
npm install jest@29.7.0 @types/jest ts-jest --save-dev

# Step 3: Initialize Tailwind CSS
npx tailwindcss init -p

# Step 4: Initialize Jest
npx ts-jest config:init

# Step 5: Add and configure Husky + lint-staged
npm install --save-dev husky lint-staged

# Enable Husky
npx husky install

# Ensure prepare script exists so Husky installs on npm install
npm pkg set scripts.prepare="husky install"

# Create pre-commit hook to run lint-staged
npx husky add .husky/pre-commit "npx lint-staged"

# Step 6: Add lint-staged config (edit your package.json and include):
# "lint-staged": {
#   "*.{js,ts,tsx}": "eslint --fix"
# }

# Final step (optional): Initialize git repo if not already
git init
git add .
git commit -m "Initial commit with setup"
