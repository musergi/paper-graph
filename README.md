# Building a knowledge tree

The approach to build such tree is based on building a graph of all the connected paper of a certain topic and
automatically generate a tree from it.

## Dataset

In order to test this solution a bid dataset is required, to do so we will use the research paper:
```
@inproceedings{lo-wang-2020-s2orc,
    title = "{S}2{ORC}: The Semantic Scholar Open Research Corpus",
    author = "Lo, Kyle  and Wang, Lucy Lu  and Neumann, Mark  and Kinney, Rodney  and Weld, Daniel",
    booktitle = "Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics",
    month = jul,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2020.acl-main.447",
    doi = "10.18653/v1/2020.acl-main.447",
    pages = "4969--4983"
}
```

The dataset of this paper can be found under the URL https://github.com/allenai/s2orc algongside the instructions to
download it. 

- [ - ] Test to download the sample files provided.
- [ - ] Read and understand content format.
- [ - ] Convert them to CSV.
- [ - ] Display relationship graph recorded in CSV.
