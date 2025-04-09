<template>
  <footer class="bg-white border-t border-gray-200">
    <div class="mx-auto max-w-7xl px-6 py-10 sm:py-12 lg:px-8">
      <div class="xl:grid xl:grid-cols-3 xl:gap-8">
        <!-- Logo + Description -->
        <div>
          <a href="#" class="flex items-center gap-2 text-lg font-semibold text-gray-900">
            QueryB
          </a>
          <p class="mt-4 text-sm text-gray-500">QueryB - Insights </p>
        </div>

        <!-- Links -->
        <div class="mt-10 grid grid-cols-2 gap-8 xl:col-span-2 xl:mt-0">
          <!--div>
            <h3 class="text-sm font-semibold text-gray-900 tracking-wider uppercase">Solutions</h3>
            <ul class="mt-4 space-y-4 text-sm text-gray-500">
              <li><a href="#" class="hover:text-gray-900">Analytics</a></li>
              <li><a href="#" class="hover:text-gray-900">Engagement</a></li>
              <li><a href="#" class="hover:text-gray-900">Security</a></li>
              <li><a href="#" class="hover:text-gray-900">Integrations</a></li>
            </ul>
          </div-->

          <!--div>
            <h3 class="text-sm font-semibold text-gray-900 tracking-wider uppercase">Company</h3>
            <ul class="mt-4 space-y-4 text-sm text-gray-500">
              <li><a href="#" class="hover:text-gray-900">About</a></li>
              <li><a href="#" class="hover:text-gray-900">Careers</a></li>
              <li><a href="#" class="hover:text-gray-900">Press</a></li>
              <li><a href="#" class="hover:text-gray-900">Contact</a></li>
            </ul>
          </div-->
        </div>
      </div>

      <!-- Bottom section -->
      <div class="mt-10 border-t border-gray-100 pt-8 text-center text-sm text-gray-500 sm:flex sm:items-center sm:justify-between">
        <p>&copy; {{ new Date().getFullYear() }} QueryB. All rights reserved.</p>
        <div class="mt-4 flex justify-center space-x-6 sm:mt-0">
          <a href="#" class="text-gray-400 hover:text-gray-500">Privacy Policy</a>
          <a href="#" class="text-gray-400 hover:text-gray-500">Terms</a>
        </div>
      </div>
    </div>
  </footer>
</template>

<script setup>
</script>
