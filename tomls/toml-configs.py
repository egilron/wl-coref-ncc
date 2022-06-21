# %% [markdown]
# ## Take the basic toml config file, and make iterations

# %%
import toml
import os
# from transformers import AutoModel, BertModel, AutoModelForMaskedLM



# %%
source = "/home/egil/gits_wsl/wl-coref-ncc/config.toml"
toml_folder = "/home/egil/gits_wsl/wl-coref-ncc/tomls"
train_path = "/home/egil/gits_wsl/ncc/wl-ncc_heads/wl-ncc_train_head.jsonl"
runpath = "/home/egil/gits_wsl/wl-coref-ncc/run.py"

with open(source) as rf:
    base_toml ={'DEFAULT': toml.loads(rf.read())['DEFAULT']}

defaults = base_toml['DEFAULT']
for key, value in defaults.items():
    print(key,":\t", value)




# %% [markdown]
# ## Changes from the default that is shared by all experiments go here

# %%
run_id = "models01"

defaults["device"] = "cpu"
defaults["bert_finetune"] = False
defaults["train_epochs"] = 2
defaults["train_data"] = train_path
defaults["dev_data"] = train_path.replace("train", "development")
defaults["test_data"] = train_path.replace("train", "test")
out_folder = os.path.join(toml_folder, run_id)
defaults["conll_log_dir"] = os.path.join(out_folder, "conll_logs")
defaults["data_dir"] = out_folder
if not os.path.exists(out_folder):
    os.mkdir(out_folder)
    if not os.path.exists(defaults["conll_log_dir"]):
        os.mkdir(defaults["conll_log_dir"])


# %% [markdown]
# ## Create lists of what should be iterated over, and write a toml file with each of these experiments in the one file
# Start without any grid, list only

# %%
alternatives = {"bert_models": ["xlm-roberta-base", "bert-base-multilingual-cased","/home/egil/datasets/norbert2", "/home/egil/datasets/nb-bert-base",]}
exp_ids = []
out_toml = {'DEFAULT': defaults}
for key, alts in alternatives.items():
    param_name = key[:-1] # Always add s also when s from before
    for idx, alt in enumerate(alts):
        experiment_id = run_id+"_"+str(idx).zfill(3)
        out_toml[experiment_id] = {param_name: alt}
        exp_ids.append(experiment_id)
out_toml_path = os.path.join(toml_folder, run_id+".toml")
with open(out_toml_path, "w") as wf:
    toml.dump(out_toml, wf)


# %% [markdown]
# ## Norwegian models
# Got them to run with cloned and local path, and torch=1.6 in stead of 1.4


# %% [markdown]
# ## Create script
# 


script_path = os.path.join(toml_folder, run_id+".sh")
scriptlines  = ["#!/bin/sh"]
for exp in exp_ids:
    scriptlines.append(" ".join(["python", runpath, "train", exp, "--config-file", out_toml_path]))

with open (script_path, "w") as wf:
    wf.write("\n".join(scriptlines))
print(script_path)
print(runpath)
print("\n".join(scriptlines))


# %%
# sudo apt-get install git-lfs
# git lfs install
# git clone https://huggingface.co/ltgoslo/norbert2



