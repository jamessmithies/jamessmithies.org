---
title: "Site Design"
layout: "list"
---

<p><span style="color:#ff0000">Update:</span> In 2026 the site was migrated from Django to <a href="https://gohugo.io/">Hugo</a>, removing the need for Docker, PostgreSQL, and Nginx. See <a href="/credits/">credits</a> for details.</p>

<p><span style="color:#ff0000">Update:</span> This site was redesigned in late 2022. It is currently a static site, hosted on GitHub. Static files are generated from a local version of the original Django site.</p>

<p><span style="color:#ff0000">Update:</span> This site was migrated to a virtual private server in late 2019, mainly to reduce security risk to my home network.</p>

<p><span style="color:#ff0000">Update:</span> This site has been running on a <a href="https://www.pine64.org/?page_id=7147" target="_blank">Rock64</a> since late 2017. It was hosted on a Raspberry Pi from late 2014.</p>

<p>jamessmithies.org was designed according to &#39;full-stack DH&#39; principles, which seek to embed values of quality, control, transparency, teachability, and verifiability at every level of the architecture. The purpose is less about rejecting the many excellent online services available to humanities researchers, and more about embracing the possibilities inherent in our contemporary global computing ecosystem: a system that remains heterogenous and empowering even as it trends towards commercialism, and governmental command and control. In that sense full-stack DH is an attempt to remind us that technical knowledge can be empowering as well as exclusionary, and that architectural choices can create products that align well to our older traditions.</p>

<p>Aside from initally using a <a href="https://www.raspberrypi.org/" target="_blank">Raspberry Pi</a> minimal computer, the open source technology used is all commercial-grade and capable of scaling up to support extraordinary levels of demand. While such technologies do not completely circumvent issues associated with the technology industry, they align well to scholarly values inherited from the humanities and social science traditions. They are also well suited to research contexts that require verifiability, falsification, and reproducibility.</p>

<p>The <a href="https://www.djangoproject.com/" target="_blank">Django</a> web framework - developed to support large newspaper sites - has been used for web development. Django is an open source project written in Python, a language frequently used to teach programming, and widely used in academic research in the social sciences, hard sciences, engineering, and the humanities.</p>

<p>The site has been built by an amateur programmer. There are plenty of things to tidy up and improve under the hood, including some embarassments. The code is available on&nbsp;<a href="http://127.0.0.1:8001/#" target="_blank">the author&#39;s GitHub account</a>. The original architecture was as follows:</p>

<p><img alt="" src="https://jsorg-docker-static.s3.amazonaws.com/media/uploads/2017/12/21/figure1_architecture-small.jpg" style="height:505px; width:747px" /></p>