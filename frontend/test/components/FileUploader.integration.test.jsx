import { render, screen, fireEvent, waitFor } from '@testing-library/react'
import FileUploader from '../../src/components/FileUploader'
import uploadService from '../../src/services/uploadService'
import { toast } from 'sonner'
import { vi } from 'vitest'

vi.mock('../../src/services/uploadService')
vi.mock('sonner', () => ({
  toast: { success: vi.fn(), error: vi.fn() },
}))

describe('FileUploader integration', () => {
  beforeEach(() => {
    vi.clearAllMocks()
  })

  it('submits text and shows success toast and result', async () => {
    uploadService.uploadText.mockResolvedValueOnce({
      categoria: 'Produtivo',
      resposta_sugerida: 'Perfeito, vamos prosseguir.'
    })

    render(<FileUploader />)

    const textarea = screen.getByPlaceholderText(/cole o conteúdo/i)
    fireEvent.change(textarea, { target: { value: 'Este é um email importante.' } })

    const button = screen.getByRole('button', { name: /enviar texto/i })
    fireEvent.click(button)

    await waitFor(() => {
      expect(uploadService.uploadText).toHaveBeenCalledWith('Este é um email importante.')
      expect(toast.success).toHaveBeenCalledWith('Analisado com sucesso!')
      expect(screen.getAllByText(/Produtivo/i).length).toBeGreaterThan(0)
      expect(screen.getByText(/Perfeito, vamos prosseguir/i)).toBeInTheDocument()
    })
  })
})
