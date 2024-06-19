# Project Title:
Voice control of Robots using Large Language Models

# Project Description:
The future of smart manufacturing hinges on robots enhancing performance and productivity, but the complex interface between humans and robots remains a challenge. Using natural language instructions to control the robots will significantly improve human-robot interaction. Despite efforts to improve the robot’s ability to interpret natural language instructions, progress has been limited due to the weak generalisation and adaptability of traditional robot programming methods. Large Language models trained on huge volumes of text data excel in Natural Language processing tasks such as semantic parsing and automatic text generation. In this study, we explored using LLMs to comprehend the basic industrial assembly instructions in natural language and convert them into low-level tasks for robots without additional training. We used the assembly instructions from the HA-ViD dataset to evaluate the performance of GPT-3.5 & Google Gemini models in semantic parsing of these instructions. The GPT-3.5 demonstrated excellent generalisation in converting previously unseen industrial assembly instructions by learning from prompts

# How to Install and Run the project

1. Install the dependencies using requirments.txt file  .

2. execute main.py file  


# Citation:
1. OpenAI. (2023). GPT-3.5: Generative Pre-trained Transformer 3.5. Retrieved from https://www.openai.com/gpt-3
2. @misc{radford2022whisper,
  doi = {10.48550/ARXIV.2212.04356},
  url = {https://arxiv.org/abs/2212.04356},
  author = {Radford, Alec and Kim, Jong Wook and Xu, Tao and Brockman, Greg and McLeavey, Christine and Sutskever, Ilya},
  title = {Robust Speech Recognition via Large-Scale Weak Supervision},
  publisher = {arXiv},
  year = {2022},
  copyright = {arXiv.org perpetual, non-exclusive license}
}
