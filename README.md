# Table of Contents

- [Table of Contents](#table-of-contents)
- [Download YouTube videos](#download-youtube-videos)
    - [Setup porject](#setup-porject)
    - [Activate virtual environment](#activate-virtual-environment)
    - [Download video](#download-video)
    - [List files in Downloads directory](#list-files-in-downloads-directory)
    - [Paste the URL](#paste-the-url)
    - [Project files structure](#project-files-structure)
    - [Details of files](#details-of-files)

# Download YouTube videos

### Setup porject

```bash
./setup/setup.py
```

### Activate virtual environment

```bash
source venv/bin/activate
```

### Download video

```bash
python download.py
```

### List files in Downloads directory

```bash
ls Downloads/
```

### Paste the URL

```url
Enter the YouTube video URL: https://www.youtube.com/xxxxxxxxxxx
```

### Project files structure

```bash
├── download.py
├── README.md
├── requirements.txt
└── setup
    └── setup.py
```

### Details of files

| FILENAME          | DESCRIPTION                                      |
|-------------------|--------------------------------------------------|
| download.py       | Script to download a YouTube video.              |
| README.md         | It has instructions on how to setup the project. |
| requirements.txt  | List of packages are saved in this file.         |
| setup/setup.py    | Script to setup the project automatically.       |
|
