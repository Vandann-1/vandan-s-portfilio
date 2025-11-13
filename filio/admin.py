from django.contrib import admin
from .models import Resume  # Import Resume model

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('name', 'pdf')
    search_fields = ('name',)

    
#           <div class="project-entry glass-card snap-start min-w-[320px] md:min-w-[400px] p-6 rounded-xl bg-[#10182d]">
#         <div class="flex flex-col items-center text-center">
#           <img src="{% static 'img/logo.jpg' %}" alt="BlogBeat" class="w-full h-40 object-cover rounded-xl mb-4" />
#           <h3 class="text-xl text-indigo-400 font-semibold">BlogBeat</h3>
#           <p class="text-gray-300 text-sm mb-3">Django + React blog platform.</p>
#           <div class="flex flex-wrap justify-center gap-2 text-xs mb-3">
#             <span class="px-2 py-1 rounded bg-indigo-700 text-white">Django</span>
#             <span class="px-2 py-1 rounded bg-indigo-700 text-white">React</span>
#             <span class="px-2 py-1 rounded bg-indigo-700 text-white">SQL</span>
#           </div>
#           <div class="flex space-x-2">
#             <a href="https://github.com/Vandann-1/blogbeat" target="_blank" class="text-sm font-medium px-4 py-2 rounded bg-indigo-600 text-white hover:bg-indigo-700 transition">GitHub</a>
#             <a href="#" class="text-sm font-medium px-4 py-2 rounded bg-green-600 text-white hover:bg-green-700 transition">Live</a>
#           </div>
#         </div>
#       </div>

#       <!-- Inventory System -->
#       <div class="project-entry glass-card snap-start min-w-[320px] md:min-w-[400px] p-6 rounded-xl bg-[#10182d]">
#         <div class="flex flex-col items-center text-center">
#           <div class="w-full h-40 bg-gray-800 rounded-xl flex items-center justify-center text-white font-bold mb-4">Coming Soon</div>
#           <h3 class="text-xl text-indigo-400 font-semibold">Inventory System</h3>
#           <p class="text-gray-300 text-sm mb-3">Stock/order manager with Django.</p>
#           <div class="flex flex-wrap justify-center gap-2 text-xs mb-3">
#             <span class="px-2 py-1 rounded bg-indigo-700 text-white">Django</span>
#             <span class="px-2 py-1 rounded bg-indigo-700 text-white">MySQL</span>
#           </div>
#           <div class="flex space-x-2">
#             <a href="#" class="text-sm font-medium px-4 py-2 rounded bg-indigo-600 text-white hover:bg-indigo-700 transition">GitHub</a>
#             <a href="#" class="text-sm font-medium px-4 py-2 rounded bg-green-600 text-white hover:bg-green-700 transition">Live</a>
#           </div>
#         </div>
#       </div>

#       <!-- TechSpire -->
#       <div class="project-entry glass-card snap-start min-w-[320px] md:min-w-[400px] p-6 rounded-xl bg-[#10182d]">
#         <div class="flex flex-col items-center text-center">
#           <img src="{% static 'img/techspire.jpg' %}" alt="TechSpire" class="w-full h-40 object-cover rounded-xl mb-4" />
#           <h3 class="text-xl text-indigo-400 font-semibold">TechSpire Solutions</h3>
#           <p class="text-gray-300 text-sm mb-3">Custom web tools with Django & WebSocket.</p>
#           <div class="flex flex-wrap justify-center gap-2 text-xs mb-3">
#             <span class="px-2 py-1 rounded bg-indigo-700 text-white">Django</span>
#             <span class="px-2 py-1 rounded bg-indigo-700 text-white">PostgreSQL</span>
#           </div>
#           <div class="flex space-x-2">
#             <a href="https://github.com/Vandann-1/techspire" target="_blank" class="text-sm font-medium px-4 py-2 rounded bg-indigo-600 text-white hover:bg-indigo-700 transition">GitHub</a>
#             <a href="#" class="text-sm font-medium px-4 py-2 rounded bg-green-600 text-white hover:bg-green-700 transition">Live</a>
#           </div>
#         </div>
#       </div>
#     </div>
#   </div>