<template>
  <div class=" min-dvh">    
    <div class="p-6">
      <h2 class="text-2xl font-semibold mb-4">Dividend Payouts - {{ selectedMonthName }} - {{ selectedYear }} </h2>
      
      <div class="flex gap-4 mb-4">
        <select v-model="selectedMonth" @change="fetchDividends" class="border rounded p-2">
          <option v-for="(m, idx) in months" :key="idx" :value="idx + 1">{{ m }}</option>
        </select>
        
        <select v-model="selectedYear" @change="fetchDividends" class="border rounded p-2">
          <option v-for="y in years" :key="y" :value="y">{{ y }}</option>
        </select>
      </div>

      <div class="overflow-x-auto bg-white shadow-md ">
        <table class="min-w-full text-sm text-left">
          <thead class="bg-gray-100 text-gray-700 uppercase text-xs">
            <tr>
              <th class="px-6 py-2 text-left">Company</th>
              <th class="px-6 py-2 text-left">Symbol</th>
              <th class="px-6 py-2 text-left">Dividend (₹)</th>
              <th class="px-6 py-2 text-left">Ex-Date</th>
              <th class="px-6 py-2 text-left">Record Date</th>
              <th class="px-6 py-2 text-left">Type</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-gray-200">
            <tr v-for="(d, i) in dividends" :key="i">
              <td class="text-left px-6 py-4" >{{ d.company }}</td>
              <td class="text-left px-6 py-4">{{ d.symbol }}</td>
              <td class="text-left px-6 py-4" >{{ d.dividend }}</td>
              <td class="text-left px-6 py-4" >{{ formatDate(d.ex_date) }}</td>
              <td class="text-left px-6 py-4" >{{ formatDate(d.record_date) }}</td>
              <td class="text-left px-6 py-4" >{{ d.type }}</td>
            </tr>
          </tbody>
        </table>
    </div>
  </div>   
</div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import axios from 'axios'

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL

const months = [
  'January', 'February', 'March', 'April', 'May', 'June',
  'July', 'August', 'September', 'October', 'November', 'December'
]

const years = Array.from({ length: 10 }, (_, i) => new Date().getFullYear() - i)

const selectedMonth = ref(new Date().getMonth() + 1)
const selectedYear = ref(new Date().getFullYear())

const selectedMonthName = computed(() => months[selectedMonth.value - 1])

const dividends = ref([])

const formatDate = (dateStr) => {
  if (!dateStr) return ''
  const date = new Date(dateStr)
  return new Intl.DateTimeFormat('en-GB', {
    day: '2-digit',
    month: 'long',
    year: 'numeric'
  }).format(date)
}

const fetchDividends = () => {
  axios
    .get(`${API_BASE_URL}/api/dividends?month=${selectedMonth.value}&year=${selectedYear.value}`)
    .then((res) => {
      dividends.value = res.data
    })
    .catch(console.error)
}

onMounted(fetchDividends)
</script>