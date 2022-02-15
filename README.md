# Gene Lookup Challenge

Create a gene lookup endpoint `/gene-lookup` in Flask that receives a human (assembly GRCh38) gene name and returns its coordinates.

The endpoint must have the following signature:

`/gene-lookup/{gene name}`

and the response should be a JSON with the following format:

```
{
  chromosome: the chromosome number where the gene is located
  start: the index representing the start of the gene interval
  end: the index representing the end of the gene interval
}
```

For example, if we would like to search the coordinates of the gene CTCF, the call would be:

`HTTP GET /gene-lookup/ctcf`

and it should return HTTP 200 with the body:

```
{
  chromosome: 16,
  start: 67562526,
  end: 67639177
}
```

Feel free to implement any response types for this endpoint that you judge necessary.

The data should be retrieved by using the ENCODE Search API to look up the Gene information.

Here's how you can access the ENCODE API to fetch the gene location:

`https://test.encodeproject.org/search/?type=Gene&field=title&field=locations&locations.assembly=GRCh38&format=json&searchTerm=<search term>`

The results of your search are returned in the `@graph` key of the API response.

You are free to use any libraries or external resources as you wish. Just please explain why you had to use them if it is not straightforward.

IMPORTANT: This endpoint is going to be used in an application with very heavy traffic and its response time should be as short as possible.


## Evaluation

Please create a Makefile with `install` and `run` clauses. The `install` clause should install all components needed for your application, and the `run` clause should start all components necessary for the server to be up and running.

Create a README.md with your submission explaining all decisions and assumptions made, and anything you would improve and why.

We are testing your submission in a Linux environment (the latest Ubuntu available).

We are looking for problem-solving skills that show you can tackle real-world technical challenges like those you may encounter in your daily work. We are also looking for code that is clean, readable, performant, and maintainable. We put significant effort into developing these criteria to ensure that, regardless of who grades the exercise, the score is an accurate reflection of the quality of the work.


## Submission:

Create a branch off this git repository and submit your solution by creating a pull request.

