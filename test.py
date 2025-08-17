name: Generate Snake

on:
  schedule: # Runs every 12 hours
    - cron: "0 */12 * * *"
  workflow_dispatch: # Allow manual trigger

jobs:
  build:
    runs-on: ubuntu-latest
    timeout: 30 minutes
    steps:
      # Checkout the repository
      - name: Checkout repository
        uses: actions/checkout@v3

      # Generate the Snake animations
      - name: Generate Snake Animation
        uses: Platane/snk@v3
        with:
          github_user_name: er-nikhil-garia
          outputs: |
            dist/github-contribution-grid-snake.svg
            dist/github-contribution-grid-snake-dark.svg?palette=github-dark
            dist/github-contribution-grid-snake-light.svg?palette=github-light
        working-directory: dist

      # Deploy Snake animations to the output branch
      - name: Push Snake Animation to Output Branch
        uses: crazy-max/ghaction-github-pages@v3.1.0
        with:
          target_branch: output
          build_dir: dist
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        continue-on-error: true