## Checking data before storage

When the bubble cam captures images, some images may not provide any insightful information. Imagine there were no bubbles or foam. As the Hydra has limited hard-disk storage, we only want to storage relevant data. During the data capturing process, we will implement a data checking mechanism to ensure we don't waste any storage space on non-meaningful data.

We can do so in a few ways

- Use ML/AI image detection
- Check filesize if above threshold

The latter option is likely more feasible and efficient.

Tasks:

- [ ] Capture many black images and look at average filesize
- [ ] Capture non-meaningful images in the wtaer and look at average filesize
