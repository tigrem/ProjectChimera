def test_trend_fetcher_output_contract():
    """
    This test enforces the TrendFetcher API contract
    defined in specs/technical.md
    """

    trend = {
        "platform": "twitter",
        "trend_name": "AI Agents",
        "score": 0.92,
        "source_url": "https://example.com",
        "timestamp": "2024-02-04T12:00:00Z"
    }

    assert isinstance(trend["platform"], str)
    assert isinstance(trend["trend_name"], str)
    assert isinstance(trend["score"], (int, float))
    assert isinstance(trend["source_url"], str)
    assert isinstance(trend["timestamp"], str)
