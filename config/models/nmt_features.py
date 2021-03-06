import tensorflow as tf
import opennmt as onmt


def model():
    return onmt.models.SequenceToSequence(
        source_inputter=onmt.inputters.ParallelInputter([
          onmt.inputters.WordEmbedder(
                    vocabulary_file_key="source_words_vocabulary",
                    embedding_size=512),
          onmt.inputters.WordEmbedder(
                    vocabulary_file_key="feature_1_vocabulary",
                    embedding_size=128),
          onmt.inputters.WordEmbedder(
                    vocabulary_file_key="feature_2_vocabulary",
                    embedding_size=32),
          onmt.inputters.WordEmbedder(
                    vocabulary_file_key="feature_3_vocabulary",
                    embedding_size=32),
          onmt.inputters.WordEmbedder(
                    vocabulary_file_key="feature_4_vocabulary",
                    embedding_size=32),
          onmt.inputters.WordEmbedder(
                    vocabulary_file_key="feature_5_vocabulary",
                    embedding_size=32),
          onmt.inputters.WordEmbedder(
                    vocabulary_file_key="feature_6_vocabulary",
                    embedding_size=32)],
          reducer=onmt.layers.ConcatReducer()),
        target_inputter=onmt.inputters.WordEmbedder(
            vocabulary_file_key="target_words_vocabulary",
            embedding_size=512),
        encoder=onmt.encoders.BidirectionalRNNEncoder(
            num_layers=3,
            num_units=1024,
            reducer=onmt.layers.ConcatReducer(),
            cell_class=tf.contrib.rnn.LSTMCell,
            dropout=0.3,
            residual_connections=False),
        decoder=onmt.decoders.AttentionalRNNDecoder(
            num_layers=3,
            num_units=1024,
            bridge=onmt.layers.DenseBridge(),
            attention_mechanism_class=tf.contrib.seq2seq.LuongAttention,
            cell_class=tf.contrib.rnn.LSTMCell,
            dropout=0.3,
            residual_connections=False))
