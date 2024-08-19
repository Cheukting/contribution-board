# contribution-board

## Set up access token as environment variables

The following tokens can be added as environment variables to add extra functionalities:

- `TOKEN`: GitHub token to increase the GitHub API request limits, useful for developing locally, can be omit when running on GitHub action. It will be something that starts with `Bearer github` followed by a unique sequence of characters. [Check here to learn how to create a GitHub access token for personal use](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

- `MASTODON_TOKEN`: Post to your Mastodon account. If you want to post to your Mastodon account when there is a new PR/ merged PR, then you have to provide your Mastodon handle in `config.py` and set up a token for access. Log in to your Mastodon account on the web browser and simply go to `https://<your_mastodon_domain>/settings/applications` to create a new application to obtain a Mastodon token. Make sure you have given `write` access to your application.

- `LINKEDIN_TOKEN`: Post to your Mastodon account. If you want to post to your Mastodon account when there is a new PR/ merged PR, then you have to follow the following steps and set up a token for access:
  1. [Create a page](https://www.linkedin.com/company/setup/new/), then [create an app](https://www.linkedin.com/developers/apps) associate with it on LinkedIn
  2. Select your app from the ["My App" page](https://www.linkedin.com/developers/apps), then under `Products` tab, request access of `Share on LinkedIn` and `Sign In with LinkedIn using OpenID Connect` under `Available products`.
  3. After getting emails that those are apprived (may take a couple of minutes), use the [LinkedIn Developer Portal Token Generator tool](https://www.linkedin.com/developers/tools/oauth/token-generator) to get a token, make sure all the permissions (email, openid, profile, w_member_social) are selected.
  4. Put your token in the environment variables as `LINKEDIN_TOKEN`.

If you are running it on GitHub action, you will need to set up these variables as secrets. [Learn how to set up secrets in GitHub Action here.](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions#creating-secrets-for-a-repository)

## Extra program needed

If you are developing locally, you will need a few extra program (not in Python) other than Python and the libraries listed at `requirements.txt` to run. They are:

- ImageMagick ([Install instruction](https://imagemagick.org/script/download.php))
- Potrace ([Intall instruction](https://potrace.sourceforge.net/#downloading))

You may want to install them before developing locally. With MacOS, both of them are also available via [Homebrew](https://brew.sh/). With Linux, you may already have ImageMagick, and Potrace is available via `apt get`

## Schedule running on GitHub action

Other than trigger by a `push` event, the GitHub action workflow is set to run every day at a certain time, the time is set randomly. To set your own time, you can do to the `generate_svg.yml` and chage the `cron` setting. To understand more about how to set the time and the best practice, [please see the guide on GitHub Action here](https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows#schedule).
