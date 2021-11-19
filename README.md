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

- [ X ] Test to download the sample files provided.
- [ X ] Read and understand content format.
- [ X ] Convert them to CSV.
- [ X ] Display relationship graph recorded in CSV.

After aalysing the sample dataset, we can see that most of the elements in the sample dataset are not interconnected
therefore this database is not usefull for our purposes. The working method still remains relevant. We are going to
attempt to generate a similar dataset but manually in order to ensure that all elements are interconnected.

The manual dataset will be connected as it will be formed by following a stream of citations. This way we will ensure
that the algorithm works and that all the nodes are interconnected.

- [ - ] Select the starting paper for manual generation
- [ - ] Generate database manually on two csv, one for meta and one for details
- [ - ] Display graph
- [ - ] Add paper titles to graph
