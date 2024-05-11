import neat
from mavisto import findMotifs

# Define a function to integrate motif discovery into NEAT algorithm
def eval_genomes(genomes, config):
    for genome_id, genome in genomes:
       
        # Load graph data
        # Assuming your graph data is stored in a dictionary called 'data'
        data = {config.data}  # Load your graph data here

        # Find motifs using mavisto library
        motif_data = findMotifs(data, config.key, config.threshold)

        # Access motif data and update genome's mutation list
        for motif_id, motif_count in motif_data.items():
            genome.mutation_list.append(('add_motif', motif_id, motif_count))


# Create the NEAT population
def run_neat_algorithm(config):
    p = neat.Population(config)

    # Add a reporter to track progress
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    # Run the NEAT algorithm
    winner = p.run(eval_genomes, 100)

    # Display the best genome
    return winner


# NEAT configuration
config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                     neat.DefaultSpeciesSet, neat.DefaultStagnation,
                     'config-feedforward')

# Call the function to run the NEAT algorithm
winner = run_neat_algorithm(config)
