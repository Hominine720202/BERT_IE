from src.tasks.infer import infer_from_trained
inferer = infer_from_trained(detect_entities=True)
test2 = "After eating the chicken, he developed a sore throat the next morning."
inferer.infer_sentence(test2, detect_entities=True)