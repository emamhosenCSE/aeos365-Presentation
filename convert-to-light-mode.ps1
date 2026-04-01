# Light Mode Conversion Script
# Converts all presentation slides from dark mode to light mode

$slidesPath = "d:\laragon\www\aeos365 Presentation\slides"

# Define color replacements
$replacements = @(
    @{ Old = 'background-color: #0f172a'; New = 'background-color: #ffffff' },
    @{ Old = 'color: white'; New = 'color: #0f172a' },
    @{ Old = 'color: #ffffff'; New = 'color: #0f172a' },
    @{ Old = 'color: #cbd5e1'; New = 'color: #4b5563' },
    @{ Old = 'color: #94a3b8'; New = 'color: #6b7280' },
    @{ Old = 'color: #64748b'; New = 'color: #9ca3af' },
    @{ Old = 'color: #e2e8f0'; New = 'color: #1f2937' },
    @{ Old = 'color: #f1f5f9'; New = 'color: #0f172a' },
    @{ Old = 'color: #b6b6b6'; New = 'color: #6b7280' },
    @{ Old = 'rgba(30, 41, 59,'; New = 'rgba(243, 244, 246,' },
    @{ Old = 'rgba(148, 163, 184,'; New = 'rgba(229, 231, 235,' },
    @{ Old = 'background-color: #1e293b'; New = 'background-color: #e5e7eb' },
    @{ Old = 'rgba(255, 255, 255, 0.03)'; New = 'rgba(0, 0, 0, 0.05)' },
    @{ Old = 'rgba(255, 255, 255, 0.05)'; New = 'rgba(0, 0, 0, 0.08)' },
    @{ Old = 'border: 1px solid rgba(255, 255, 255'; New = 'border: 1px solid rgba(0, 0, 0' },
    @{ Old = 'color: #60a5fa'; New = 'color: #0369a1' },
    @{ Old = 'color: #93c5fd'; New = 'color: #0369a1' },
    @{ Old = 'color: #bfdbfe'; New = 'color: #0369a1' },
    @{ Old = 'color: #fca5a5'; New = 'color: #dc2626' },
    @{ Old = 'color: #fed7aa'; New = 'color: #92400e' },
    @{ Old = 'color: #d8b4fe'; New = 'color: #0369a1' },
    @{ Old = 'color: #a8a29e'; New = 'color: #6b7280' },
    @{ Old = 'color: #e9d5ff'; New = 'color: #0f172a' },
    @{ Old = 'color: #cffafe'; New = 'color: #0369a1' },
    @{ Old = 'color: #67e8f9'; New = 'color: #0369a1' },
    @{ Old = 'color: #d1fae5'; New = 'color: #166534' },
    @{ Old = 'color: #34d399'; New = 'color: #16a34a' },
    @{ Old = 'color: #cbd5e1'; New = 'color: #374151' },
    @{ Old = 'text-shadow: 0 0 30px'; New = 'text-shadow: none;' },
    @{ Old = 'backdrop-filter: blur'; New = 'backdrop-filter: none;' }
)

# Get all HTML files in slides folder
$files = Get-ChildItem "$slidesPath\*.html" -Exclude "0_cover.html", "1.html", "2.html", "3.html"

$count = 0
foreach ($file in $files) {
    Write-Host "Processing: $($file.Name)"
    $content = Get-Content $file.FullName -Raw
    
    foreach ($replacement in $replacements) {
        $content = $content -Replace [regex]::Escape($replacement.Old), $replacement.New
    }
    
    Set-Content $file.FullName -Value $content
    $count++
    Write-Host "  ✓ Converted"
}

Write-Host "`nConversion complete! Processed $count files."
