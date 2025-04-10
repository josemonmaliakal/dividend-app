<template>
  <div class="grow p-6 lg:rounded-lg lg:bg-white lg:p-10 lg:ring-1 lg:shadow-xs lg:ring-zinc-950/5 dark:lg:bg-zinc-900 dark:lg:ring-white/10">
    <div class="mx-auto max-w-6xl">
      <div class="flex items-end justify-between gap-4">
        <h1 class="text-2xl/8 font-semibold text-zinc-950 sm:text-xl/8 dark:text-white">
          Dividend Payouts | {{ selectedMonthName }}  {{ selectedYear }}
        </h1>
        <div class="flex gap-4">
          <select v-model="selectedMonth" @change="fetchDividends" class="border rounded p-2">
            <option v-for="(m, idx) in months" :key="idx" :value="idx + 1">{{ m }}</option>
          </select>        
          <select v-model="selectedYear" @change="fetchDividends" class="border rounded p-2">
            <option v-for="y in years" :key="y" :value="y">{{ y }}</option>
          </select>
        </div>
      </div>
    <div class="flow-root">
      <div class="overflow-x-auto">
  <table class="min-w-full divide-y divide-gray-200 text-sm">
    <thead class="bg-gray-100">
      <tr>
        <th class="px-6 py-3 text-left font-medium text-gray-700">Name</th>
        <th class="px-6 py-3 text-left font-medium text-gray-700">Title</th>
        <th class="px-6 py-3 text-left font-medium text-gray-700">Email</th>
        <th class="px-6 py-3 text-left font-medium text-gray-700">Role</th>
      </tr>
    </thead>
    <tbody class="divide-y divide-gray-200">
      <tr>
        <td class="px-6 py-4 whitespace-nowrap">John Doe</td>
        <td class="px-6 py-4 whitespace-nowrap">Software Engineer</td>
        <td class="px-6 py-4 whitespace-nowrap">john@example.com</td>
        <td class="px-6 py-4 whitespace-nowrap">Admin</td>
      </tr>
      <tr>
        <td class="px-6 py-4 whitespace-nowrap">Jane Smith</td>
        <td class="px-6 py-4 whitespace-nowrap">Product Manager</td>
        <td class="px-6 py-4 whitespace-nowrap">jane@example.com</td>
        <td class="px-6 py-4 whitespace-nowrap">Editor</td>
      </tr>
    </tbody>
  </table>
</div>


      <div class="mt-8 whitespace-nowrap">
        <div class="overflow-x-auto">
          <table class="min-w-full text-sm text-left  text-sm/6 divide-y divide-gray-200"  >
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