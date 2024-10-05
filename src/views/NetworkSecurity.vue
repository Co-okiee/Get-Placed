<template>
    <div class="network-security-container">
      <h1 class="main-title">Network Security and Cryptography Layer</h1>
      <p class="intro">
        Network Security encompasses the policies, practices, and technologies aimed at protecting networks and data from unauthorized access, attacks, and damage. Cryptography is a critical component of network security that provides confidentiality, integrity, and authenticity of data.
      </p>

      <h2 class="sub-title">The CIA Triad</h2>
      <p class="content">
        The CIA triad is a model for understanding the core principles of information security: Confidentiality, Integrity, and Availability. 
      </p>

      <h2 class="sub-title">Introduction to Firewall</h2>
      <p class="content">
        A firewall is a network security device that monitors and controls incoming and outgoing network traffic based on predetermined security rules.
      </p>

      <h2 class="sub-title">Types of Firewalls and Possible Attacks</h2>
      <ul class="characteristics-list">
        <li><strong>Packet-Filtering Firewalls:</strong> Examine packets and allow or deny them based on source/destination IP addresses and ports.</li>
        <li><strong>Stateful Inspection Firewalls:</strong> Track the state of active connections and make decisions based on the context of the traffic.</li>
        <li><strong>Proxy Firewalls:</strong> Intercept and inspect traffic before it reaches the intended destination.</li>
      </ul>

      <h2 class="sub-title">Firewall Methodologies</h2>
      <p class="content">
        Firewalls can employ various methodologies including filtering, proxying, and stateful inspection to manage network traffic effectively.
      </p>

      <h2 class="sub-title">Zone-Based Firewall</h2>
      <p class="content">
        A zone-based firewall segregates the network into multiple zones and applies security policies to control traffic between these zones.
      </p>

      <h2 class="sub-title">Zone-Based Firewall Configuration</h2>
      <p class="content">
        Configuration involves defining zones, associating interfaces with zones, and applying policies to govern traffic flow.
      </p>

      <h2 class="sub-title">How to Set Up a Firewall in Linux?</h2>
      <p class="content">
        To set up a firewall in Linux, tools like iptables or firewalld can be used. Basic commands involve defining rules for incoming and outgoing traffic.
      </p>

      <h2 class="sub-title">Message Authentication Codes (MAC)</h2>
      <p class="content">
        MACs provide a way to ensure the integrity and authenticity of a message through a shared secret key.
      </p>

      <h2 class="sub-title">How Message Authentication Code Works?</h2>
      <p class="content">
        MACs work by combining the message and a secret key to produce a fixed-size hash that is sent along with the message. The recipient can verify the integrity by computing the MAC again.
      </p>

      <h2 class="sub-title">HMAC Algorithm</h2>
      <p class="content">
        HMAC (Hash-based Message Authentication Code) uses a cryptographic hash function and a secret key to provide both data integrity and authenticity.
      </p>

      <h2 class="sub-title">Password Authentication Protocol (PAP)</h2>
      <p class="content">
        PAP is a simple authentication protocol that transmits passwords in plaintext, making it vulnerable to interception.
      </p>

      <h2 class="sub-title">Basic Network Attacks</h2>
      <ul class="characteristics-list">
        <li><strong>Denial of Service (DoS):</strong> Attacks aimed at making a network service unavailable.</li>
        <li><strong>Vishing:</strong> Voice phishing that exploits phone calls to deceive victims into providing personal information.</li>
        <li><strong>Birthday Attack:</strong> A type of cryptographic attack that exploits the mathematics behind the probability of collisions in hash functions.</li>
      </ul>

      <h2 class="sub-title">System Security</h2>
      <p class="content">
        System security involves measures taken to protect a system from unauthorized access or damage, ensuring data integrity and confidentiality.
      </p>

      <h2 class="sub-title">Private Browsing</h2>
      <p class="content">
        Private browsing modes in web browsers prevent the storage of browsing history and cookies, offering users an extra layer of privacy.
      </p>

      <h2 class="sub-title">Threat Modelling</h2>
      <p class="content">
        Threat modelling is the process of identifying potential threats to a system and defining measures to mitigate these threats.
      </p>

      <h2 class="sub-title">DFD Based Threat Modelling | Set 1</h2>
      <p class="content">
        Data Flow Diagrams (DFDs) help visualize data flow in a system, aiding in identifying potential vulnerabilities.
      </p>

      <h2 class="sub-title">DFD Based Threat Modelling | Set 2</h2>
      <p class="content">
        Further DFD analysis allows for a deeper understanding of interactions and vulnerabilities within a system.
      </p>

      <h2 class="sub-title">Types of Viruses</h2>
      <ul class="characteristics-list">
        <li><strong>File Infector Virus:</strong> Attaches itself to executable files.</li>
        <li><strong>Macro Virus:</strong> Infects documents and templates.</li>
        <li><strong>Polymorphic Virus:</strong> Changes its code to avoid detection.</li>
      </ul>

      <h2 class="sub-title">Denial of Service and Prevention</h2>
      <p class="content">
        Preventative measures against DoS attacks include rate limiting, traffic analysis, and robust firewall configurations.
      </p>

      <h2 class="sub-title">Denial of Service (DDoS) Attack</h2>
      <p class="content">
        DDoS attacks involve multiple compromised systems attacking a single target, making it difficult to mitigate.
      </p>

      <h2 class="sub-title">Unicode</h2>
      <p class="content">
        Unicode is a standardized encoding system for text that ensures consistency across different platforms and languages.
      </p>

      <h2 class="sub-title">RC4 Encryption Algorithm</h2>
      <p class="content">
        RC4 is a stream cipher known for its simplicity and speed but is considered less secure compared to modern algorithms.
      </p>

      <h2 class="sub-title">RSA Algorithm in Cryptography</h2>
      <p class="content">
        RSA is a widely used asymmetric encryption algorithm based on the mathematical difficulty of factoring large integers.
      </p>

      <h2 class="sub-title">RSA Algorithm using Multiple Precision Arithmetic Library</h2>
      <p class="content">
        Using libraries allows for handling very large integers necessary for RSA encryption and decryption processes.
      </p>

      <h2 class="sub-title">Weak RSA Decryption with Chinese-Remainder Theorem</h2>
      <p class="content">
        The Chinese-Remainder Theorem can be used to improve the efficiency of RSA decryption under certain conditions.
      </p>

      <h2 class="sub-title">How to Solve RSA Algorithm Problems?</h2>
      <p class="content">
        RSA problems typically involve generating keys, encrypting messages, and decrypting them using the private key.
      </p>

      <h2 class="sub-title">Hash Functions in System Security</h2>
      <p class="content">
        Hash functions create fixed-size hash values from variable-size data, ensuring data integrity and verifying authenticity.
      </p>

      <h2 class="sub-title">DNA Cryptography</h2>
      <p class="content">
        DNA cryptography utilizes the unique properties of DNA sequences to create secure cryptographic keys.
      </p>

      <h2 class="sub-title">RC5 Encryption Algorithm</h2>
      <p class="content">
        RC5 is a block cipher known for its variable block size, key size, and number of rounds, providing flexibility and security.
      </p>

      <h2 class="sub-title">ElGamal Encryption Algorithm</h2>
      <p class="content">
        ElGamal is an asymmetric key encryption algorithm based on the Diffie-Hellman key exchange, offering security through randomness.
      </p>

      <h2 class="sub-title">Caesar Cipher</h2>
      <p class="content">
        The Caesar Cipher is a simple substitution cipher that shifts letters in the alphabet by a fixed number of places.
      </p>

      <h2 class="sub-title">Cryptography Introduction</h2>
      <p class="content">
        Cryptography is the practice of securing communication and information through encoding and decoding messages.
      </p>

      <h2 class="sub-title">Cryptography | Traditional Symmetric Ciphers</h2>
      <p class="content">
        Traditional symmetric ciphers use the same key for both encryption and decryption, such as DES and AES.
      </p>

      <h2 class="sub-title">Block Cipher Modes of Operation</h2>
      <p class="content">
        Modes like ECB, CBC, and CTR define how block ciphers process data, affecting security and efficiency.
      </p>

      <h2 class="sub-title">Cryptography | Development of Cryptography</h2>
      <p class="content">
        Cryptography has evolved from simple manual techniques to complex algorithms designed to secure digital communication.
      </p>

      <h2 class="sub-title">Difference between AES and DES Ciphers</h2>
      <p class="content">
        AES is a more secure and efficient algorithm than DES, which has become outdated due to its shorter key length.
      </p>

      <h2 class="sub-title">Transforming a Plain Text Message to Cipher Text</h2>
      <p class="content">
        Transforming involves applying a cipher algorithm to plaintext, resulting in ciphertext that is unreadable without decryption.
      </p>

      <h2 class="sub-title">What is Cryptocurrency?</h2>
      <p class="content">
        Cryptocurrency is a digital or virtual currency that uses cryptography for security and operates on a decentralized network.
      </p>

      <h2 class="sub-title">Introduction to Crypto-Terminologies</h2>
      <p class="content">
        Understanding key terms such as blockchain, wallets, and mining is crucial for comprehending the cryptocurrency landscape.
      </p>

      <h2 class="sub-title">Quantum Cryptography</h2>
      <p class="content">
        Quantum cryptography leverages quantum mechanics to create secure communication channels resistant to eavesdropping.
      </p>

      <h2 class="sub-title">End-to-End Encryption (E2EE) in Computer Networks</h2>
      <p class="content">
        E2EE ensures that data transmitted between two endpoints is encrypted, preventing interception by third parties.
      </p>

      <h2 class="sub-title">IP Security (IPSec)</h2>
      <p class="content">
        IPSec is a framework for securing Internet Protocol (IP) communications through encryption and authentication.
      </p>

      <h2 class="sub-title">What is Packet Sniffing?</h2>
      <p class="content">
        Packet sniffing involves capturing and analyzing packets transmitted over a network, often used for network troubleshooting and security monitoring.
      </p>

      <h2 class="sub-title">Introduction to Sniffers</h2>
      <p class="content">
        Sniffers are tools that capture and analyze network traffic, which can be used for both legitimate and malicious purposes.
      </p>

      <h2 class="sub-title">Data Encryption Standard (DES) | Set 1</h2>
      <p class="content">
        DES is a symmetric-key algorithm that encrypts data in 64-bit blocks using a 56-bit key.
      </p>

      <h2 class="sub-title">End-to-End Encryption (E2EE) in Computer Network</h2>
      <p class="content">
        E2EE provides secure data transmission by ensuring that only the communicating users can read the messages.
      </p>

      <h2 class="sub-title">Types of Security Attacks | Active and Passive Attacks</h2>
      <p class="content">
        Active attacks involve modifying the data in transit, while passive attacks involve eavesdropping without altering the data.
      </p>

      <h2 class="sub-title">Types of Wireless and Mobile Device Attacks</h2>
      <ul class="characteristics-list">
        <li><strong>Man-in-the-Middle Attack:</strong> An attacker intercepts and potentially alters communication between two parties.</li>
        <li><strong>Evil Twin Attack:</strong> A rogue Wi-Fi access point mimicking a legitimate one to steal sensitive information.</li>
      </ul>

      <h2 class="sub-title">Types of Email Attacks</h2>
      <ul class="characteristics-list">
        <li><strong>Phishing:</strong> Fraudulent emails trick users into revealing personal information.</li>
        <li><strong>Spear Phishing:</strong> Targeted phishing attacks aimed at specific individuals.</li>
      </ul>

      <h2 class="sub-title">Sybil Attack</h2>
      <p class="content">
        A Sybil attack occurs when a single adversary creates multiple identities to gain a disproportionately large influence on a network.
      </p>

      <h2 class="sub-title">Malware and Its Types</h2>
      <ul class="characteristics-list">
        <li><strong>Virus:</strong> Attaches to files and spreads when those files are executed.</li>
        <li><strong>Worm:</strong> Self-replicating malware that spreads across networks.</li>
        <li><strong>Trojan Horse:</strong> Disguises itself as legitimate software to gain unauthorized access.</li>
      </ul>

      <h2 class="sub-title">Useful Links</h2>
      <h3 class="link-title">YouTube Tutorials</h3>
      <ul>
        <li><a href="https://www.youtube.com/watch?v=security1" target="_blank">Introduction to Network Security (English)</a></li>
        <li><a href="https://www.youtube.com/watch?v=security2" target="_blank">Cryptography Basics in Hindi</a></li>
      </ul>

      <h2 class="sub-title">Diagrams</h2>
      <p>Below are some diagrams that illustrate the concepts discussed:</p>
      <div class="diagram-container">
        <img src="path/to/diagram1.png" alt="Diagram illustrating the CIA triad" />
        <img src="path/to/diagram2.png" alt="Diagram showing firewall types" />
        <img src="path/to/diagram3.png" alt="Diagram of encryption algorithms" />
      </div>
    </div>
</template>

<script>
export default {
    name: "NetworkSecurityAndCryptography",
};
</script>

<style scoped>
.network-security-container {
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