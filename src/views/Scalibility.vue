<template>
    <div class="sd-container">
        <h1 class="main-title">Scalability in System Design</h1>
        <p class="intro">
            Scalability in system design refers to the capability of a system to handle a growing amount of work, or its potential to accommodate growth. It is essential for ensuring that applications can manage increased loads without compromising performance.
        </p>

        <h2 class="sub-title">What is Scalability and How to Achieve It</h2>
        <p class="content">
            Scalability is the ability of a system to expand its capacity and performance as demand increases. It can be achieved through various strategies, such as adding resources (vertical scaling) or distributing the load across multiple systems (horizontal scaling).
        </p>
        
        <h2 class="sub-title">Which Scalability Approach is Right for Our Application?</h2>
        <p class="content">
            Choosing the right scalability approach depends on the application’s architecture and specific requirements. Consider factors like the expected load, budget, and the ability to modify existing infrastructure when determining whether to scale vertically or horizontally.
        </p>

        <h2 class="sub-title">Primary Bottlenecks that Hurt the Scalability of an Application</h2>
        <ul class="characteristics-list">
            <li><strong>Database Bottlenecks:</strong> Heavy read/write operations can slow down performance.</li>
            <li><strong>Network Latency:</strong> High latency can hinder communication between distributed components.</li>
            <li><strong>Resource Contention:</strong> Competition for CPU, memory, and I/O resources can lead to degraded performance.</li>
            <li><strong>Single Points of Failure:</strong> Relying on a single server or service can lead to bottlenecks and outages.</li>
        </ul>

        <h2 class="sub-title">Examples of Scalability in System Design</h2>
        <p class="content">
            <strong>Example 1:</strong> An e-commerce website scales horizontally by adding more servers to handle increased traffic during sales events.<br>
            <strong>Example 2:</strong> A video streaming service uses a Content Delivery Network (CDN) to distribute content globally, reducing load on the main servers and improving access speeds.
        </p>
        
        <h2 class="sub-title">Diagrams</h2>
        <p>Below are some diagrams that illustrate scalability concepts:</p>
        <div class="diagram-container">
            <img src="path/to/scalability_diagram1.png" alt="Vertical Scaling Diagram" />
            <img src="path/to/scalability_diagram2.png" alt="Horizontal Scaling Diagram" />
            <img src="path/to/scalability_diagram3.png" alt="Scalability Bottleneck Diagram" />
        </div>
        
        <h2 class="sub-title">Useful Links</h2>
        <h3 class="link-title">YouTube Tutorials</h3>
        <ul>
            <li><a href="https://www.youtube.com/watch?v=scalability1" target="_blank">Understanding Scalability in System Design (English)</a></li>
            <li><a href="https://www.youtube.com/watch?v=scalability2" target="_blank">Scalability Explained in Hindi</a></li>
        </ul>
    </div>
</template>

<script>
export default {
    name: "ScalabilityInSystemDesign",
};
</script>

<style scoped>
.sd-container {
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