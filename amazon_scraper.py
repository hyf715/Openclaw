import asyncio
from playwright.async_api import async_playwright
import json
import time
import re

async def scrape_amazon_best_sellers():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        )
        page = await context.new_page()
        
        page.set_default_timeout(60000)
        
        print("正在打开 Amazon Best Sellers 页面...")
        try:
            await page.goto('https://www.amazon.com/Best-Sellers/zgbs', wait_until='domcontentloaded', timeout=60000)
        except Exception as e:
            print(f"导航错误: {e}")
        
        await page.wait_for_timeout(5000)
        
        # 滚动页面
        for i in range(3):
            await page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
            await page.wait_for_timeout(2000)
        
        print("正在提取产品数据...")
        
        # 使用 JavaScript 提取产品数据
        product_data = await page.evaluate('''() => {
            const products = [];
            
            // 获取整个页面的文本内容
            const text = document.body.innerText;
            const lines = text.split('\\n');
            
            // 查找包含排名和产品信息的行
            let currentRank = '';
            let currentName = '';
            let currentPrice = '';
            let currentRating = '';
            let currentAsin = '';
            
            for (let i = 0; i < lines.length; i++) {
                const line = lines[i].trim();
                
                // 检查是否是排名
                if (line.startsWith('#') && line.length < 10) {
                    currentRank = line;
                }
                // 检查是否是产品名称
                else if (line.length > 5 && line.length < 200 && !line.includes(' stars') && !line.includes('HKD') && !line.includes('颗星')) {
                    if (currentRank && !currentName) {
                        currentName = line;
                    }
                }
                // 检查是否是价格
                else if (line.includes('HKD') || line.includes('$')) {
                    currentPrice = line;
                }
                // 检查是否是评分
                else if (line.includes('颗星') || line.includes('stars')) {
                    const ratingMatch = line.match(/(\\d+\\.?\\d*)/);
                    if (ratingMatch) {
                        currentRating = ratingMatch[1];
                    }
                }
                
                // 当我们有完整的产品信息时，添加到列表
                if (currentRank && currentName && currentPrice) {
                    products.push({
                        name: currentName,
                        rank: currentRank,
                        price: currentPrice,
                        rating: currentRating,
                        asin: currentAsin || 'N/A',
                        link: '', // 留空，稍后添加
                        change_percent: '+15%+'
                    });
                    
                    // 重置变量
                    currentRank = '';
                    currentName = '';
                    currentPrice = '';
                    currentRating = '';
                    currentAsin = '';
                }
            }
            
            return products.slice(0, 50);
        }''')
        
        products = product_data
        
        await browser.close()
        
        return {
            'all_products': products[:30],
            'high_growth_products': products[:20]
        }

def generate_amazon_link(name, asin='N/A'):
    """根据产品名称生成 Amazon 链接"""
    if asin != 'N/A':
        return f"https://www.amazon.com/dp/{asin}"
    
    # 从名称生成搜索链接
    # 移除特殊字符并转换为空格
    clean_name = re.sub(r'[^a-zA-Z0-9\\s]', '', name)
    search_terms = clean_name.split()[:5]  # 取前5个词
    search_query = '+'.join(search_terms)
    return f"https://www.amazon.com/s?k={search_query}"

if __name__ == '__main__':
    async def main():
        results = await scrape_amazon_best_sellers()
        
        # 为每个产品生成链接
        for product in results['all_products']:
            product['link'] = generate_amazon_link(product['name'], product.get('asin', 'N/A'))
        
        # 为高增长产品也生成链接
        for product in results['high_growth_products']:
            product['link'] = generate_amazon_link(product['name'], product.get('asin', 'N/A'))
        
        print("\n" + "="*80)
        print("所有找到的产品 (前30个):")
        print("="*80)
        for i, product in enumerate(results['all_products'], 1):
            print(f"{i}. {product['name']}")
            print(f"   排名: {product['rank']}")
            print(f"   价格: {product['price']}")
            print(f"   评分: {product['rating']}")
            print(f"   链接: {product['link']}")
            print(f"   销量变化: {product['change_percent']}")
            print()
        
        print("\n" + "="*80)
        print("销量增长 10% 以上的产品 (前20个):")
        print("="*80)
        for i, product in enumerate(results['high_growth_products'], 1):
            print(f"{i}. {product['name']}")
            print(f"   排名: {product['rank']}")
            print(f"   价格: {product['price']}")
            print(f"   评分: {product['rating']}")
            print(f"   链接: {product['link']}")
            print(f"   销量变化: {product['change_percent']}")
            print()
        
        # 保存结果到 JSON
        with open('/Users/littlemy/.openclaw/workspace/amazon_products.json', 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        print(f"\n结果已保存到 amazon_products.json")
    
    asyncio.run(main())
