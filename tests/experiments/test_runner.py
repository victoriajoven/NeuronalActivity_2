from unittest.mock import MagicMock, call

import src.experiments.runner as runner


def test_run_all_experiments(monkeypatch):
    # ---- Mocks ----

    mock_jobs = [["fake_job"]]
    mock_instance = MagicMock()
    mock_best = MagicMock()
    mock_best.fitness = 123
    mock_history = MagicMock()
    mock_result = MagicMock()
    mock_plot = MagicMock()

    # parse_orlib_jobshop
    mock_parse = MagicMock(return_value=mock_jobs)
    monkeypatch.setattr(runner, "parse_orlib_jobshop", mock_parse)

    # JobShopInstance
    mock_js_instance = MagicMock(return_value=mock_instance)
    monkeypatch.setattr(runner, "JobShopInstance", mock_js_instance)

    # Experiment
    mock_experiment = MagicMock()
    mock_experiment.run.return_value = (mock_best, mock_history)

    mock_experiment_cls = MagicMock(return_value=mock_experiment)
    monkeypatch.setattr(runner, "Experiment", mock_experiment_cls)
    
    # Results and plotting
    mock_save_result = MagicMock(return_value=mock_result)
    monkeypatch.setattr(runner, "save_result", mock_save_result)
    mock_plot_fitness = MagicMock(return_value=mock_plot)
    monkeypatch.setattr(runner, "plot_fitness_evolution", mock_plot_fitness)
    

    # ---- Act ----
    runner.run_all_experiments()

    # ---- Assert ----

    # 3 datasets parsed
    assert mock_parse.call_count == 3
    assert mock_js_instance.call_count == 3

    # 1 config by dataset
    assert mock_experiment_cls.call_count == 18

    # Check calls to Experiment with correct parameters
    assert mock_experiment.run.call_count == 18

