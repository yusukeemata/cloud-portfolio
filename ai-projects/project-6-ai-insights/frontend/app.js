// app.js - Portfolio Project #6 AI Pipeline Orchestrator
document.addEventListener('DOMContentLoaded', () => {
    // ⚠️ Replace this string with your deployed API Gateway Invoke URL once staged
    const API_ENDPOINT = 'YOUR_API_GATEWAY_INVOKE_URL_HERE/insights';

    const newsTitle = document.getElementById('news-title');
    const newsDesc = document.getElementById('news-desc');
    const newsLink = document.getElementById('news-link');
    const pmbokAnalysis = document.getElementById('analysis-content');

    // Fetch analytical insights asynchronously from serverless infrastructure
    async function fetchAIInsights() {
        try {
            const response = await fetch(API_ENDPOINT, {
                method: 'GET',
                headers: { 'Accept': 'application/json' }
            });

            if (!response.ok) {
                throw new Error(`HTTP network error: Status ${response.status}`);
            }

            const data = await response.json();
            
            // Render source technical news metrics safely
            newsTitle.textContent = data.target_news.title;
            newsTitle.classList.remove('loading-skeleton');
            newsLink.href = data.target_news.link;
            newsLink.style.display = 'inline-block';

            // Render LLM generative PMBOK analysis insights
            pmbokAnalysis.innerHTML = `<p style="white-space: pre-wrap;">${data.pmbok_analysis}</p>`;
            pmbokAnalysis.classList.remove('loading-skeleton');

        } catch (error) {
            console.error('Failed to resolve serverless pipeline data:', error);
            newsTitle.textContent = 'Data Pipeline Synchronization Deferred';
            pmbokAnalysis.innerHTML = `<span style="color: #ef4444;">Infrastructure timeout or authorization pending. Please retry shortly.</span>`;
        }
    }

    fetchAIInsights();
});
