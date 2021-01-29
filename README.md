<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
***
***
***
*** To avoid retyping too much info. Do a search and replace for the following:
*** CreatePhotonW, htmlmthcases, @CreatePhotonW, email, HtmlmthCases, Cases for HTMLMTH
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
<!--
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
-->


<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/CreatePhotonW/htmlmthcases">
<!--    <img src="images/logo.png" alt="Logo" width="80" height="80"> -->
  </a>

  <h3 align="center">HtmlmthCases</h3>

  <p align="center">
    Cases for [HTMLMTH](https://github.com/CreatePhotonW/htmlmth)
    <br />
<!--    <a href="https://github.com/CreatePhotonW/htmlmthcases"><strong>Explore the docs »</strong></a> -->
    <br />
    <br />
    <!--
    <a href="https://github.com/CreatePhotonW/htmlmthcases">View Demo</a>
    ·
    -->
    <a href="https://github.com/CreatePhotonW/htmlmthcases/issues">Report Bug</a>
    ·
    <a href="https://github.com/CreatePhotonW/htmlmthcases/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<!--
[![Product Name Screen Shot][product-screenshot]](https://example.com)
-->

Cases for [HTMLMTH](https://github.com/CreatePhotonW/htmlmth)

<!-- 
### Built With

* []()
* []()
* []()

-->



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

See [htmlmth Prerequisites](https://github.com/CreatePhotonW/htmlmth#prerequisites)

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/CreatePhotonW/HtmlmthCases.git
   ```
2. Clone the htmlmth repo
   ```sh
   git clone https://github.com/CreatePhotonW/Htmlmth.git
   ```
3. Follow [htmlmth Installation](https://github.com/CreatePhotonW/htmlmth#installation)

<!-- USAGE EXAMPLES -->
## Usage

See [htmlmth Usage](https://github.com/CreatePhotonW/htmlmth#usage)


Run [_scripting_encoder_server.py_](https://github.com/CreatePhotonW/htmlmth/blob/main/scripting_encoder_server.py) from htmlmth is applicable. See htmlmth's readme for more info.
```bash
python.exe -m pip install flask
set FLASK_APP=scripting_encoder_server.py
python.exe -m flask run --host=0.0.0.0
```

Follow html instructions for *EvasionHTTPServer.py* or *output_cases.py* 

Specifically, select a baseline file and case file and specify your selection with the **-b** and **-c** options

For example,
```sh
rm -r out ; mkdir out ; ./htmlmth/htmlmth/output_cases.py -sesp 5000 -sesh 172.30.112.1 -sesp 5000 -o out -b htmlmthcases/sets/1/baselines/CVE-2014-6332_v3.html -c htmlmthcases/sets/1/cases/HtmlEvasion/cve_2014_6332_v3.py -ld
```

```sh
./htmlmth/htmlmth/EvasionHTTPServer.py -i 0.0.0.0 -p 8000 -sesp 5000 -sesh 172.30.112.1 -sesp 5000 -b htmlmthcases/sets/1/baselines/CVE-2014-6332_v3.html -c htmlmthcases/sets/1/cases/HtmlEvasion/cve_2014_6332_v3.py -tc HtmlEvasion-html-320
```

**Note**

Cases may be tailored for specified baselines.

In the extreme case of ContentEvasion cases, an arbitrary baseline cannot be used.

In most other cases you can use the cases built for one baseline with another baseline.

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/CreatePhotonW/htmlmthcases/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

CreatePhotonW - [@CreatePhotonW](https://twitter.com/CreatePhotonW)

Project Link: [https://github.com/CreatePhotonW/htmlmthcases](https://github.com/CreatePhotonW/htmlmthcases)



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/CreatePhotonW/repo.svg?style=for-the-badge
[contributors-url]: https://github.com/CreatePhotonW/repo/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/CreatePhotonW/repo.svg?style=for-the-badge
[forks-url]: https://github.com/CreatePhotonW/repo/network/members
[stars-shield]: https://img.shields.io/github/stars/CreatePhotonW/repo.svg?style=for-the-badge
[stars-url]: https://github.com/CreatePhotonW/repo/stargazers
[issues-shield]: https://img.shields.io/github/issues/CreatePhotonW/repo.svg?style=for-the-badge
[issues-url]: https://github.com/CreatePhotonW/repo/issues
[license-shield]: https://img.shields.io/github/license/CreatePhotonW/repo.svg?style=for-the-badge
[license-url]: https://github.com/CreatePhotonW/repo/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/CreatePhotonW
