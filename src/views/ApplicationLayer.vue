<template>
    <div class="app-container">
      <h1 class="main-title">Application Layer</h1>
      <p class="intro">
        The Application Layer is the topmost layer of the OSI model, responsible for providing network services directly to end-user applications. It enables software applications to communicate over a network.
      </p>
  
      <h2 class="sub-title">Protocols in Application Layer</h2>
      <ul class="characteristics-list">
        <li><strong>Simple Mail Transfer Protocol (SMTP):</strong> A protocol used for sending emails between servers.</li>
        <li><strong>DNS (Domain Name System):</strong> Translates domain names into IP addresses.</li>
        <li><strong>Dynamic Host Configuration Protocol (DHCP):</strong> Dynamically assigns IP addresses to devices on a network.</li>
        <li><strong>File Transfer Protocol (FTP):</strong> Used for transferring files between a client and a server.</li>
        <li><strong>Simple Network Management Protocol (SNMP):</strong> A protocol for managing devices on IP networks.</li>
      </ul>
  
      <h2 class="sub-title">Why Does DNS Use UDP and Not TCP?</h2>
      <p class="content">
        DNS primarily uses UDP for its queries because it is faster and requires less overhead than TCP. Most DNS queries are small and do not require the reliability that TCP provides, making UDP a better choice for these operations.
      </p>
  
      <h2 class="sub-title">Address Resolution in DNS</h2>
      <p class="content">
        Address resolution is the process of translating a domain name into its corresponding IP address through the DNS, allowing users to access websites by name instead of by numerical address.
      </p>
  
      <h2 class="sub-title">DNS Spoofing or DNS Cache Poisoning</h2>
      <p class="content">
        DNS spoofing is a technique where an attacker corrupts the DNS cache to redirect users to malicious sites. This can compromise security and privacy by misleading users.
      </p>
  
      <h2 class="sub-title">Types of DNS Attacks and Tactics for Security</h2>
      <p class="content">
        Common types of DNS attacks include DNS spoofing, DDoS attacks, and amplification attacks. Implementing measures such as DNSSEC (Domain Name System Security Extensions) can help mitigate these risks.
      </p>
  
      <h2 class="sub-title">What’s the Difference Between http:// and https://?</h2>
      <p class="content">
        The primary difference is that HTTPS (HyperText Transfer Protocol Secure) provides a secure communication channel over the Internet through encryption, while HTTP does not.
      </p>
  
      <h2 class="sub-title">What’s the Difference Between HTML and HTTP?</h2>
      <p class="content">
        HTML (HyperText Markup Language) is a markup language used to create web pages, while HTTP is a protocol used for transferring data over the web.
      </p>
  
      <h2 class="sub-title">HTTP Non-Persistent & Persistent Connection</h2>
      <p class="content">
        Non-persistent connections open a new TCP connection for each request/response pair, while persistent connections keep the connection open for multiple requests, reducing latency.
      </p>
  
      <h2 class="sub-title">Asynchronous Transfer Mode (ATM)</h2>
      <p class="content">
        ATM is a network technology that uses fixed-size cells for data transmission, ensuring consistent performance and support for various data types, including voice and video.
      </p>
  
      <h2 class="sub-title">What is Local Host?</h2>
      <p class="content">
        Local host refers to the computer that is currently being used. It is typically accessed via the loopback IP address (127.0.0.1), which allows network applications to communicate with the local machine.
      </p>
  
      <h2 class="sub-title">DHCP Relay Agent</h2>
      <p class="content">
        A DHCP relay agent forwards DHCP requests and replies between clients and servers, especially when the server is on a different subnet from the client.
      </p>
  
      <h2 class="sub-title">How DHCP Server Dynamically Assigns IP Address to a Host?</h2>
      <p class="content">
        The DHCP server assigns IP addresses dynamically through a process that includes discovering available addresses, offering an address to a client, and acknowledging the allocation, allowing devices to connect to the network easily.
      </p>
  
      <h2 class="sub-title">What’s the Difference Between The Internet and The Web?</h2>
      <p class="content">
        The Internet is the global network of interconnected computers, while the Web (World Wide Web) is a collection of information accessed via the Internet, using HTTP to transfer data.
      </p>
  
      <h2 class="sub-title">Multipurpose Internet Mail Extensions (MIME)</h2>
      <p class="content">
        MIME extends the format of email messages to support text in character sets other than ASCII, as well as attachments of audio, video, and image files.
      </p>
  
      <h2 class="sub-title">Computer Network | MIME Media Types</h2>
      <p class="content">
        MIME media types define the nature and format of a document, file, or byte stream. This helps in identifying the type of data being sent over the Internet, ensuring it is handled correctly by applications.
      </p>
  
      <h2 class="sub-title">Quality of Service and Multimedia</h2>
      <p class="content">
        Quality of Service (QoS) ensures that multimedia applications, like video and audio streaming, receive sufficient bandwidth and low latency for optimal performance, prioritizing their data over other types.
      </p>
  
      <h2 class="sub-title">Web Caching and the Conditional GET Statements</h2>
      <p class="content">
        Web caching stores copies of web pages to reduce load times for subsequent requests. Conditional GET statements help browsers determine if a cached version is up-to-date, minimizing unnecessary data transfer.
      </p>
  
      <h2 class="sub-title">Useful Links</h2>
      <h3 class="link-title">YouTube Tutorials</h3>
      <ul>
        <li><a href="https://www.youtube.com/watch?v=app1" target="_blank">Introduction to Application Layer (English)</a></li>
        <li><a href="https://www.youtube.com/watch?v=app2" target="_blank">Application Layer Protocols in Hindi</a></li>
      </ul>
  
      <h2 class="sub-title">Diagrams</h2>
      <p>Below are some diagrams that illustrate the concepts discussed:</p>
      <div class="diagram-container">
        <img src="path/to/dns_overview.png" alt="Overview of DNS Resolution Process" />
        <img src="path/to/http_vs_https.png" alt="Difference between HTTP and HTTPS" />
        <img src="path/to/dhcp_process.png" alt="DHCP Address Assignment Process" />
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "ApplicationLayer",
  };
  </script>
  
  <style scoped>
  .app-container {
    max-width: 900px;
    margin: 20px auto;
    padding: 20px;
    border-radius: 10px;
    background-color: #121212;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.6);
    font-family: 'Roboto', sans-serif;
    color: #e0e0e0;
    line-height: 1.6;
  }
  
  .main-title {
    font-size: 2.8em;
    color: #ffcc00;
    text-align: center;
    margin-bottom: 30px;
  }
  
  .sub-title {
    font-size: 2.2em;
    color: #e0ce46;
    margin-top: 40px;
    padding-bottom: 10px;
  }
  
  .content {
    font-size: 1.2em;
    margin-bottom: 20px;
  }
  
  .characteristics-list {
    margin: 10px 0;
    padding-left: 20px;
    font-size: 1.2em;
  }
  
  li {
    margin-bottom: 15px;
    line-height: 1.6;
  }
  
  .diagram-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    margin: 20px 0;
  }
  
  .diagram-container img {
    max-width: 100%;
    height: auto;
    margin-bottom: 10px;
    border: 2px solid #e0ce46; /* border color for diagrams */
  }
  
  a {
    color: #ddc452;
    text-decoration: none;
    font-size: 1.1em;
  }
  
  a:hover {
    text-decoration: underline;
  }
  
  .link-title {
    color: #ffffff;
    margin-top: 30px;
  }
  </style>