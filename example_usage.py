from client import DynamicSparkpageLayoutSynthesizerClient

def main():
    client = DynamicSparkpageLayoutSynthesizerClient()
    res = client.synthesize_sparkpage_layout('Top 10 Humanoid AI Robots 2026', 8)
    print('Sparkpage Synthesizer: ' + res['layout_id'] + ' (' + res['search_topic'] + ')')
    print('Cards: ' + str(res['rendered_entity_cards']) + ' | Columns: ' + str(res['comparison_matrix_columns']))
    print('Live Preview: ' + res['sparkpage_live_preview_url'])

if __name__ == '__main__':
    main()
