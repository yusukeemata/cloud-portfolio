// app.js - Portfolio Project #6 AI Pipeline Orchestrator
document.addEventListener('DOMContentLoaded', () => {
    const API_ENDPOINT = 'https://16s42opvi7.execute-api.us-east-1.amazonaws.com/prod/insights';

    const fetchBtn = document.getElementById('fetch-btn');
    const translateBtn = document.getElementById('translate-btn'); // 翻訳ボタン要素を取得
    const insightsContainer = document.getElementById('insights-container');

    // 取得したデータを一時保存（キャッシュ）するオブジェクト
    let currentInsights = {
        en: "",
        ja: ""
    };
    let isJapanese = false;

    // Fetch analytical insights asynchronously from serverless infrastructure
    async function fetchAIInsights() {
        // 1. ローディング状態の表示＆翻訳ボタンの非表示
        if (translateBtn) translateBtn.style.display = 'none';

        insightsContainer.innerHTML = `
            <div class="loading-status">
                <span style="display: inline-block; animation: spin 1s linear infinite; margin-right: 8px;">⏳</span> 
                Analyzing the latest tech trends against PMBOK 8th framework...
            </div>`;
        fetchBtn.disabled = true;
        fetchBtn.textContent = 'Processing Pipeline...';

        try {
            const response = await fetch(API_ENDPOINT, {
                method: 'GET',
                headers: { 'Accept': 'application/json' }
            });

            if (!response.ok) {
                throw new Error(`HTTP network error: Status ${response.status}`);
            }

            const data = await response.json();
            
            // データを変数に保持（Lambdaから返ってきた英語と日本語）
            currentInsights.en = data.pmbok_analysis || '';
            currentInsights.ja = data.pmbok_analysis_ja || '';

            // 2. HTML構造に合わせた綺麗なカード型UIの動的生成（初期状態は英語）
            insightsContainer.innerHTML = `
                <div class="insight-card">
                    <span class="insight-meta">Latest AWS Ingestion</span>
                    <h3 id="news-title">${data.target_news.title}</h3>
                    <div style="margin-bottom: 15px;">
                        <a id="news-link" href="${data.target_news.link}" target="_blank" style="color: #0284c7; text-decoration: underline; font-size: 14px;">
                            View AWS Official What's New Source ↗
                        </a>
                    </div>
                    <hr style="border: 0; border-top: 1px solid rgba(0,0,0,0.1); margin: 20px 0;">
                    <span class="insight-meta" style="background: #f0fdf4; color: #16a34a;">PMBOK 8th Edition Strategic Analysis</span>
                    <div class="insight-body" id="analysis-content" style="white-space: pre-wrap; font-family: sans-serif; margin-top: 10px;">${currentInsights.en.split('\n').map(l => l.trim()).join('\n')}</div>
                </div>`;

            // 3. データ取得完了後、翻訳ボタンを表示
            if (translateBtn && currentInsights.ja) {
                isJapanese = false;
                translateBtn.textContent = "日本語にする（Amazon Translate）";
                translateBtn.style.display = 'inline-flex';
            }

        } catch (error) {
            console.error('Failed to resolve serverless pipeline data:', error);
            insightsContainer.innerHTML = `
                <div class="insight-card" style="border-left: 5px solid #ef4444;">
                    <h3 style="color: #ef4444;">Pipeline Synchronization Deferred</h3>
                    <p class="insight-body" style="color: #ef4444;">
                        An error occurred while calling the backend: ${error.message}<br><br>
                        Please ensure Bedrock model access and daily token quotas are active on the AWS side.
                    </p>
                </div>`;
        } finally {
            fetchBtn.disabled = false;
            fetchBtn.textContent = 'Fetch Latest AI Insights';
        }
    }

    // 4. 翻訳ボタンクリック時の超高速テキスト切り替え処理
    if (translateBtn) {
    translateBtn.addEventListener('click', () => {
        const analysisContent = document.getElementById('analysis-content');
        if (!analysisContent) return;

        if (isJapanese) {
            // 日本語 → 英語に戻す（スペース除去処理付き）
            analysisContent.textContent = currentInsights.en.split('\n').map(l => l.trim()).join('\n');
            translateBtn.textContent = "日本語にする（Amazon Translate）";
            isJapanese = false;
        } else {
            // 英語 → 日本語に切り替え（スペース除去処理付き）
            analysisContent.textContent = currentInsights.ja.split('\n').map(l => l.trim()).join('\n');
            translateBtn.textContent = "英語に戻す";
            isJapanese = true;
        }
    });
}

    // ボタンのクリックイベントを紐付け
    fetchBtn.addEventListener('click', fetchAIInsights);
});
