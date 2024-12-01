<template>
  <div class="company-container">
    <div class="nav-header">
      <button @click="goBack" class="back-button">
        <span class="back-icon">←</span>
        Back to Quiz Options
      </button>
    </div>

    <div class="header-section">
      <h1 class="main-title">Company Specific Preparation</h1>
      <p class="subtitle">Select a company to prepare for</p>
    </div>

    <div class="company-buttons-container">
      <div v-for="company in companies" :key="company.name" class="company-button" @click="goToCompanyQuiz(company.name)">
        <img :src="company.logo" alt="Company Logo" class="company-logo" />
        <span>{{ company.name }}</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "CompanySpecific",
  data() {
    return {
      companies: [
        { name: "Barclays", logo: "https://imgs.search.brave.com/IekZ4r35gjaVZj2s_UDLxcsuxBRuxEpnCBYNNgrDN4U/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9pY29u/cy52ZXJ5aWNvbi5j/b20vcG5nL28vYnVz/aW5lc3MvYmFuay1s/b2dvLWNvbGxlY3Rp/b24vYmFyY2xheXMt/bG9nby5wbmc" },
        { name: "DeutscheBank", logo: "https://1000logos.net/wp-content/uploads/2017/09/Deutsche-Bank-Logo-768x432.png" },
        { name: "JPMorgan", logo: "https://imgs.search.brave.com/ge-iqc-sUFNd8s1qclNbvtRLcFeRNFZ9GiqUENNHkpU/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9sb2dv/cy13b3JsZC5uZXQv/d3AtY29udGVudC91/cGxvYWRzLzIwMjEv/MDIvSlAtTW9yZ2Fu/LUNoYXNlLVN5bWJv/bC03MDB4Mzk0LnBu/Zw" },
        { name: "Accenture", logo: "https://imgs.search.brave.com/hOzpKIM4SLhSritMlf51kTV_cJNKAu6wjZnv_MQ7QXo/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9jb21w/YW5pZXNsb2dvLmNv/bS9pbWcvb3JpZy9B/Q04tY2NlNWI0MTEu/cG5nP3Q9MTcyMDI0/NDQ5MA" },
        { name: "TCS", logo: "https://companieslogo.com/img/orig/TCS.NS-7401f1bd.png?t=1720244494" },
        { name: "Oracle", logo: "https://imgs.search.brave.com/X458aERa0Ew2-7LZ_LBKZkK7UV0R1_cAc4dWeSTJhbo/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9hc3Nl/dHMuc3RpY2twbmcu/Y29tL3RodW1icy82/MmJjN2FmNjA3MWRl/YzE3ODQ5YWYzMjMu/cG5n" },
        { name: "Wipro", logo: "https://imgs.search.brave.com/YUv5s65ONu03_6x9yfyLqpKPrRPT6XPvdvSEww8qqSU/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly93d3cu/cG5naXRlbS5jb20v/cGltZ3MvbS8xOTMt/MTkzMjY5OV93aXBy/by1sb2dvLXBuZy10/cmFuc3BhcmVudC1w/bmcucG5n" },
        { name: "Cognizant", logo: "https://seeklogo.com/images/C/Cognizant_Technology_Solutions-logo-525DD9ECA8-seeklogo.com.png" },
        { name: "Google", logo: "https://lh3.googleusercontent.com/COxitqgJr1sJnIDe8-jiKhxDx1FrYbtRHKJ9z_hELisAlapwE9LUPh6fcXIfb5vwpbMl4xl9H9TRFPc5NOO8Sb3VSgIBrfRYvW6cUA" },
        { name: "Microsoft", logo: "https://imgs.search.brave.com/R9W6ytA6CRPIO6CcQwJpXjtre717-s3x4uBEb_46awU/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9wbmdp/bWcuY29tL3VwbG9h/ZHMvbWljcm9zb2Z0/L21pY3Jvc29mdF9Q/TkcxMy5wbmc" },
        { name: "Amazon", logo: "https://imgs.search.brave.com/mmIIy0_mCFuT6m4imGJYqS3X7LYywXvDvcmGv6eVzuU/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9mcmVl/bG9nb3BuZy5jb20v/aW1hZ2VzL2FsbF9p/bWcvMTY4ODM2MTA1/NWFtYXpvbi1sb2dv/LXBuZy5wbmc" },
        { name: "Siemens", logo: "https://www.logo.wine/a/logo/Siemens/Siemens-Logo.wine.svg" },
        { name: "NVIDIA", logo: "https://imgs.search.brave.com/GtMCG93WrGb04SoOlgri1-Wh5M5pXzJzBv9aJki9jPo/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9hc3Nl/dHMuc3RpY2twbmcu/Y29tL2ltYWdlcy82/MDg5NWVjN2Q1OThh/NTAwMDQ0OGVhOTcu/cG5n" },
        { name: "Deloitte", logo: "https://imgs.search.brave.com/I1fhSwiSid9AUPoek8nTxO_b9CJz6NCgTaYyft7ELe8/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9icmFu/ZHNsb2dvcy5jb20v/d3AtY29udGVudC91/cGxvYWRzL2ltYWdl/cy9kZWxvaXR0ZS1s/b2dvLnBuZw" },
        { name: "Airtel", logo: "https://imgs.search.brave.com/uALGABYJYt8IDTyIM7R3Mdj1-a-NaDWGAaPS_FefgOE/rs:fit:500:0:0:0/g:ce/aHR0cHM6Ly9zZWVr/bG9nby5jb20vaW1h/Z2VzL0EvYWlydGVs/LWxvZ28tQUVGRjk0/MjI3Ni1zZWVrbG9n/by5jb20ucG5n" },
      ],
    };
  },
  methods: {
    goToCompanyQuiz(companyName) {
        // Updated list with correct names matching the routes
        const companiesWithDedicatedLanding = [
            'Barclays',
            'DeutscheBank', // Updated to match the route naming
            'JPMorgan', // Updated to match the route naming
            'Accenture',
            'TCS',
            'Oracle',
            'Wipro',
            'Cognizant',
            'Google',
            'Microsoft',
            'Amazon',
            'Siemens',
            'NVIDIA', // Corrected case to match the route
            'Deloitte',
            'Airtel'
        ];
        
        // Check if the company is in the list
        if (companiesWithDedicatedLanding.includes(companyName)) {
            // Format the name to create the route name
            const formattedName = companyName.toLowerCase().replace(/ /g, '-');
            this.$router.push({ name: `${formattedName}-landing` });
        } else {
            this.$router.push({ name: 'company-quiz', params: { companyName } });
        }
    },

    goBack() {
      this.$router.push({ name: "quiz-options" });
    }
  }
};
</script>

<style scoped>
.company-container {
  min-height: 100vh;
  background: linear-gradient(135deg, #000000 0%, #393939 100%);
  padding: 4rem 2rem 2rem;
  text-align: center;
}

.nav-header {
  position: absolute; 
  top: 1rem;
  left: 1rem; 
  z-index: 10; 
  color: #ffffff;
}

.back-button {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: white;
  border: 1px solid #e2e8f0;
  padding: 0.75rem 1.5rem;
  border-radius: 8px;
  color: #1e293b;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s ease;
}

.back-button:hover {
  background: #f1f5f9;
  transform: translateX(-4px);
}

.back-icon {
  font-size: 1.2rem;
}

.main-title {
  font-size: 2.5rem;
  font-weight: 700;
  color: #d6d7d7;
  margin-bottom: 0.5rem;
}

.subtitle {
  color: #cacaca;
  font-size: 1.1rem;
}

.header-section {
  text-align: center;
  margin: 3rem 0 3rem; /* This sets margin-top to 3rem, adjust as needed */
}


.company-buttons-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 2rem;
  margin-top: 2rem;
}

.company-button {
  display: flex;
  align-items: center;
  background: rgb(251, 251, 251);
  border-radius: 16px;
  padding: 1rem;
  width: 200px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.company-button:hover {
  transform: translateY(-5px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.company-logo {
  width: 40px; /* Set a fixed width */
  height: auto; /* Maintain aspect ratio */
  max-height: 40px; /* Set a max height */
  object-fit: contain; /* Ensure the entire logo fits */
  margin-right: 1rem;
}

.company-button span {
  color: #1e293b; /* Ensure text is visible */
  font-weight: 500; /* Optional: make it bolder */
}
</style>
