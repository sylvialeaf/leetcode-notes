# daily_push.ps1 — 每日刷题打卡：把当天改动一键提交并推到 GitHub
# 用法（在 H:\leetcode 目录下）：
#   .\daily_push.ps1                  → 自动用「study: 2026-06-21 刷题打卡」当提交信息
#   .\daily_push.ps1 "做了双指针3题"   → 用你写的这句话当提交信息
#
# 第一次运行如果报「无法加载...执行策略」，先跑一次这句解禁（只需一次）：
#   Set-ExecutionPolicy -Scope CurrentUser RemoteSigned

param([string]$msg = "")

if ([string]::IsNullOrWhiteSpace($msg)) {
    $today = Get-Date -Format "yyyy-MM-dd"
    $msg = "study: $today 刷题打卡"
}

git add -A
git commit -m $msg
if ($LASTEXITCODE -ne 0) {
    Write-Host "（今天没有改动，不用打卡。去做一道题再来～）" -ForegroundColor Yellow
    exit 0
}
git push
Write-Host "✅ 打卡成功！绿点 +1 → https://github.com/sylvialeaf/leetcode-notes" -ForegroundColor Green
