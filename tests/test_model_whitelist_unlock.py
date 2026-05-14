from pathlib import Path


def test_renderer_script_unlocks_custom_config_model_from_model_whitelist():
    text = Path("codex_session_delete/inject/renderer-inject.js").read_text(encoding="utf-8")

    assert "modelWhitelistUnlock: true" in text
    assert "data-codex-plus-setting=\"modelWhitelistUnlock\"" in text
    assert "/codex-model-catalog" in text
    assert "loadCodexModelCatalog" in text
    assert "/v1/models" in text
    assert "patchCodexModelWhitelist" in text
    assert "codexPlusModelDescriptor" in text
    assert "model/list" in text
    assert "includeHidden: true" in text
    assert "codexPlusModelListRequestIds" in text
    assert "patchStatsigModelWhitelist" in text
    assert "available_models" in text
    assert "patchReactModelState" in text
