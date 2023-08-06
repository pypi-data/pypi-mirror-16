"""Core Genetic Algorithm classes.

Contents
--------

:GeneticAlgorithm: The base class from which all GA behaviors inherit.

"""
#from builtins import str
#from builtins import range
#from builtins import object

import argparse
import random
import uuid

# pylint: disable=too-many-instance-attributes
class GeneticAlgorithm(object):
    """Base class from which all genetic features inherit.

    And yes, it *is* hard to talk about OO inheritance and genetics without
    making bad puns.
    """

    def __init__(self, config={}):
        """Initialize a genetic algorithm.

        Args:
            config (Dict): Configuration values to control behavior and setup
                the problem space.

        """

        self.id = uuid.uuid4()
        self.iteration = 0
        self.config = config
        self.population = None
        self.next_generation = []
        self.random = random.Random()

        # Basic GA parameters
        self.population_size = self.config.setdefault("population_size", 50)
        self.mutation_prob = self.config.setdefault("mutation_prob", 0.20)
        self.crossover_prob = self.config.setdefault("crossover_prob", 0.80)
        self.max_iterations = self.config.setdefault("max_iterations", 50)
        if self.max_iterations <= 0:
            self.max_iterations = 1

        # Use a static random seed
        if "seed" in self.config:
            self.random.seed(self.config["seed"])

    @classmethod
    def arg_parser(self):
        """Add arguments to an ``ArgumentParser`` object for configuration."""
        parser = argparse.ArgumentParser(add_help=False)

        parser.add_argument("--population-size", "-p", type=int,
                            help="Size of the population")
        parser.add_argument("--iterations", "-i", type=int,
                            dest="max_iterations",
                            help="Maximum number of iterations")
        parser.add_argument("--mutation", "-m", type=float,
                            dest="mutation_prob",
                            help="Mutation probability (0.0-1.0)")
        parser.add_argument("--crossover", "-c", type=float,
                            dest="crossover_prob",
                            help="Crossover probability (0.0-1.0)")
        parser.add_argument("--seed", "-s",
                            help="Seed for random number generator")

        return parser

    def seed(self):
        """Create an initial seed population."""
        if self.population is None:
            self.population = []
            for _ in range(0, self.population_size):
                self.population.append(self.create())

    def score_population(self):
        """Return a scored and ranked copy of the population.

        This scores the fitness of each member of the population and returns
        the complete population as ``[(member, score)]``.

        Raises:
            Exception: If the population is empty.
        """

        if self.population is None:
            raise Exception("Cannot score and rank an empty population.")

        scored = [(member, self.fitness(member)) for member in self.population]
        scored.sort(key=lambda n: n[1])
        scored.reverse()

        return scored

    def solve(self):
        """Run the GA until complete and return the best solution.

        Returns:
            Any: The best chromosome in the last generation.
        """
        if self.population is None:
            self.seed()

        try:
            while not self.is_finished():
                self.iteration += 1
                self.pre_generate()
                self.generate()
                self.post_generate()

        except KeyboardInterrupt:
            pass

        return self.best()

    def is_finished(self):
        """Return true while there have been fewer iterations than the max.

        This is the most basic stop condition for a GA.
        """
        return self.iteration >= self.max_iterations

    def generate(self):
        """Create and assign a new generation as the population."""
        while len(self.next_generation) < self.population_size:
            ticket = self.random.random()
            if ticket < self.crossover_prob:
                child = self.crossover()

            elif ticket < self.crossover_prob + self.mutation_prob:
                child = self.select()
                child = self.mutate(child)

            else:
                child = self.select()

            self.next_generation.append(child)

    def fitness(self, chromosome):
        return self.score(chromosome)

    def pre_generate(self):
        """Do anything necessary before creating the next generation."""
        pass

    def post_generate(self):
        """Do anything necessary after creating a generation."""
        self.population = list(self.next_generation)
        self.next_generation = []

    def best(self):
        """Returns the fittest member in the population of a GA.

        This implementation will rank the whole population and select the
        chromosome with the highest fitness score.
        """
        return self.score_population()[0][0]

    def mutate(self, chromosome):
        """Return a mutated chromosome."""
        raise NotImplementedError

    def select(self):
        """Return a chromosome from the current generation.

        This is used for crossover/recombination, so more fit members should
        be selected more often.
        """
        raise NotImplementedError

    def create(self):
        """Create a new chromosome for the population.

        This is invoked when seeding the initial population.
        """
        raise NotImplementedError

    def crossover(self):
        """Return a new chromosome created via crossover.

        The parent chromosomes should be found using `select()`.
        """
        raise NotImplementedError

    def score(self, chromosome):
        """Return the score of a chromosome."""
        raise NotImplementedError

    def chromosome_str(self, chromosome):
        """Return a readable string representation of a chromosome.

        The representation should be human-readable, so expand domain terms.
        For instance, rather than return a binary string, return a list of
        features and whether or not they're enabled.

        This method should include the chromosome's fitness score and/or its
        components when using an aggregate score.
        """
        raise NotImplementedError

    def chromosome_repr(self, chromosome):
        """Return an unambiguous representation of a chromosome.

        The score should *not* be included, and domain terminology should be
        omitted.
        """
        return self.chromosome_str(chromosome)

    def __str__(self):
        import inspect
        return str(inspect.getmro(self.__class__)) + str(self.config)

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)
