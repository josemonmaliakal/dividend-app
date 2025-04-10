<template>
  
    <Header />
    <main>
    <div class="mx-auto max-w-7xl    lg:bg-white  lg:rounded-lg lg:mt-2 lg:mb-2">
     <DividendTable :month="month" :year="year" :monthName="monthName" />    
    </div>
    </main>
    <Footer />
  
</template>

<script setup>
import Header from './components/Header.vue'
import DividendTable from './components/DividendTable.vue'
import Footer from './components/Footer.vue'

const today = new Date()
const month = today.getMonth() + 1
const year = today.getFullYear()
const monthNames = [
  "None","January", "February", "March", "April", "May", "June",
  "July", "August", "September", "October", "November", "December"
]
const monthName = monthNames[month]
</script>
